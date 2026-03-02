import os
import random
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import discord
from discord import app_commands
from dotenv import load_dotenv

from questions import PROBLEMS

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


@dataclass
class Session:
    """Tracks a user's active quiz session."""
    problem: dict
    current_part: int
    score: int
    total_points: int
    active: bool


sessions: Dict[int, Session] = {}


def check_answer(user_val: float, correct_val: float, tolerance: float = 0.05) -> bool:
    """Check if user_val is within ±tolerance of correct_val."""
    if correct_val == 0:
        return abs(user_val) < 1e-10
    return abs(user_val - correct_val) / abs(correct_val) <= tolerance


def parse_number(text: str) -> Optional[float]:
    """Parse a number from user input, supporting scientific notation like 3.5e27."""
    text = text.strip().replace(" ", "")
    # Support common input patterns: 3.5*10^27, 3.5x10^27
    text = text.replace("×", "*").replace("x", "*").replace("X", "*")
    if "*10^" in text:
        parts = text.split("*10^")
        try:
            base = float(parts[0])
            exp = float(parts[1])
            return base * (10 ** exp)
        except (ValueError, IndexError):
            return None
    try:
        return float(text)
    except ValueError:
        return None


def build_part_embed(problem: dict, part_idx: int) -> discord.Embed:
    """Build an embed for a given sub-part of a problem."""
    part = problem["parts"][part_idx]
    total_parts = len(problem["parts"])

    embed = discord.Embed(
        title=f"Q{problem['number']} — {problem['title']}",
        color=0x5865F2,
    )
    embed.add_field(
        name=f"Part {part['label']}  [{part['points']} pts]",
        value=part["text"],
        inline=False,
    )
    embed.set_footer(
        text=f"Sub-part {part_idx + 1}/{total_parts} • Answer with /astro_answer"
    )
    return embed


# ── Discord client setup ─────────────────────────────────────────────────────

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")


# ── /astro_start ─────────────────────────────────────────────────────────────

@tree.command(name="astro_start", description="Start an astrophysics quiz problem")
async def astro_start(interaction: discord.Interaction):
    problem = random.choice(PROBLEMS)

    sessions[interaction.user.id] = Session(
        problem=problem,
        current_part=0,
        score=0,
        total_points=sum(p["points"] for p in problem["parts"]),
        active=True,
    )

    # Send intro text
    intro_embed = discord.Embed(
        title=f"🔭  Q{problem['number']} — {problem['title']}",
        description=problem["intro"],
        color=0x5865F2,
    )

    # Send figure if available
    files = []
    if problem.get("figure"):
        fig_file = discord.File(problem["figure"])
        intro_embed.set_image(url=f"attachment://{os.path.basename(problem['figure'])}")
        files.append(fig_file)

    await interaction.response.send_message(embed=intro_embed, files=files)

    # If there is a second figure (Q76), send it as a follow-up
    if problem.get("figure2"):
        fig2_file = discord.File(problem["figure2"])
        fig2_embed = discord.Embed(color=0x5865F2)
        fig2_embed.set_image(
            url=f"attachment://{os.path.basename(problem['figure2'])}"
        )
        await interaction.followup.send(embed=fig2_embed, file=fig2_file)

    # Send the first sub-part
    part_embed = build_part_embed(problem, 0)
    await interaction.followup.send(embed=part_embed)


# ── /astro_answer ────────────────────────────────────────────────────────────

@tree.command(name="astro_answer", description="Submit your answer (numerical value)")
@app_commands.describe(value="Your numerical answer (supports scientific notation, e.g. 3.5e27)")
async def astro_answer(interaction: discord.Interaction, value: str):
    await interaction.response.defer()

    session = sessions.get(interaction.user.id)
    if not session or not session.active:
        await interaction.followup.send(
            "You don't have an active quiz. Use `/astro_start` to begin!", ephemeral=True
        )
        return

    part = session.problem["parts"][session.current_part]
    parsed = parse_number(value)

    if parsed is None:
        await interaction.followup.send(
            "❓ Couldn't parse that as a number. Try formats like `9660`, `3.5e27`, or `2.84*10^-11`.",
            ephemeral=True,
        )
        return

    correct = part["answer"]
    is_correct = check_answer(parsed, correct)

    if is_correct:
        session.score += part["points"]
        response = (
            f"✅ **Correct!** {part['label']} = `{correct}` {part['unit']}  "
            f"(+{part['points']} pts)"
        )
    else:
        response = (
            f"❌ **Incorrect.** The answer was `{correct}` {part['unit']}.  "
            f"You answered `{parsed}`."
        )

    # Advance to next part
    session.current_part += 1

    if session.current_part >= len(session.problem["parts"]):
        # Quiz complete
        session.active = False
        await interaction.followup.send(
            f"{response}\n\n"
            f"🏁 **Quiz complete!**\n"
            f"Final Score: **{session.score} / {session.total_points}** points"
        )
        return

    # Show next sub-part
    next_embed = build_part_embed(session.problem, session.current_part)
    await interaction.followup.send(response, embed=next_embed)


# ── /astro_skip ──────────────────────────────────────────────────────────────

@tree.command(name="astro_skip", description="Skip the current sub-part (scores 0)")
async def astro_skip(interaction: discord.Interaction):
    await interaction.response.defer()

    session = sessions.get(interaction.user.id)
    if not session or not session.active:
        await interaction.followup.send(
            "You don't have an active quiz. Use `/astro_start` to begin!", ephemeral=True
        )
        return

    part = session.problem["parts"][session.current_part]
    response = (
        f"⏭️ **Skipped** {part['label']}. The answer was `{part['answer']}` {part['unit']}."
    )

    session.current_part += 1

    if session.current_part >= len(session.problem["parts"]):
        session.active = False
        await interaction.followup.send(
            f"{response}\n\n"
            f"🏁 **Quiz complete!**\n"
            f"Final Score: **{session.score} / {session.total_points}** points"
        )
        return

    next_embed = build_part_embed(session.problem, session.current_part)
    await interaction.followup.send(response, embed=next_embed)


# ── /astro_stop ──────────────────────────────────────────────────────────────

@tree.command(name="astro_stop", description="End your quiz early and see your score")
async def astro_stop(interaction: discord.Interaction):
    session = sessions.get(interaction.user.id)
    if not session or not session.active:
        await interaction.response.send_message(
            "You don't have an active quiz.", ephemeral=True
        )
        return

    session.active = False
    answered = session.current_part
    total = len(session.problem["parts"])

    await interaction.response.send_message(
        f"🛑 **Quiz ended early.**\n"
        f"You answered **{answered}/{total}** sub-parts.\n"
        f"Score: **{session.score} / {session.total_points}** points"
    )


# ── Run ──────────────────────────────────────────────────────────────────────

client.run(TOKEN)
