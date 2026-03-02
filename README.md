# 🔭 AstroQuizBot

A Discord bot for practicing **Science Olympiad Astrophysics** calculation problems. Presents multi-part problems from the CMU test with numerical answer checking (±5% tolerance).

## Features

- **Calculation-based quiz** — Multi-part astrophysics problems with figures
- **4 problems, 26 sub-parts** — Covering stellar properties, orbital mechanics, binary stars, and transits
- **±5% tolerance** — Answers within 5% of the correct value are accepted
- **Scientific notation** — Supports inputs like `3.5e27` or `2.84*10^-11`
- **Score tracking** — Points per sub-part, final score at the end
- **Slash commands** — Clean Discord slash command interface

## Commands

| Command | Description |
|---------|-------------|
| `/astro_start` | Start a random astrophysics problem |
| `/astro_answer <value>` | Submit your numerical answer |
| `/astro_skip` | Skip the current sub-part (scores 0) |
| `/astro_stop` | End the quiz early and see your score |

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AstroQuizBot.git
   cd AstroQuizBot
   ```

2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Add your Discord bot token**
   
   Edit the `.env` file:
   ```
   DISCORD_TOKEN=your_token_here
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

## Tech Stack

- **Python** + [discord.py](https://discordpy.readthedocs.io/)
- **python-dotenv** for environment variable management

## Problems Included

| # | Topic | Sub-parts | Points |
|---|-------|-----------|--------|
| Q73 | Star Kappist — Wien's law, luminosity, redshift | 7 | 18 |
| Q74 | Planet Mirad a — Kepler's laws, orbital mechanics, magnitudes | 9 | 28 |
| Q75 | Binary stars Zenor I & II — radial velocity, masses | 6 | 18 |
| Q76 | Transit of Spectris a — flux ratio, transit geometry | 4 | 16 |
