"""
Question bank for AstroQuizBot — CMU Science Olympiad Astrophysics Test.

Each problem is a dict with:
  - "number": question number (73–76)
  - "title": short title for display
  - "intro": introductory text shown at the start
  - "figure": optional path to the figure image
  - "parts": list of sub-parts, each a dict with:
      - "label": e.g. "(a)"
      - "text": question text
      - "answer": correct numerical answer (float)
      - "unit": display unit string
      - "points": point value
"""

PROBLEMS = [
    {
        "number": 73,
        "title": "Star Kappist — Stellar Properties",
        "intro": (
            "**Question 73 (18 points)** — Refer to Figure 1.\n\n"
            "Figure 1 shows the spectrum graph of star **Kappist**. "
            "The radius of this star is **1.8 R☉**."
        ),
        "figure": "images/fig1_kappist_spectrum.png",
        "parts": [
            {
                "label": "(a)",
                "text": "Based on this data, find the **temperature** of Kappist in **kelvins**.",
                "answer": 9660.0,
                "unit": "K",
                "points": 2,
            },
            {
                "label": "(b)",
                "text": "Find the **luminosity** of Kappist in **watts**.",
                "answer": 9.729e27,
                "unit": "W",
                "points": 2,
            },
            {
                "label": "(c)",
                "text": (
                    "If the temperature of Kappist was arbitrarily decreased to 5000 K, "
                    "what would be the new wavelength at which the flux peaks in **nanometers**?"
                ),
                "answer": 579.6,
                "unit": "nm",
                "points": 4,
            },
            {
                "label": "(d)",
                "text": (
                    "If planet Kappist a is 2 AU away from Kappist and has a radius of "
                    "0.5 R_Earth, what **fraction** of the light from Kappist reaches Kappist a?"
                ),
                "answer": 2.84e-11,
                "unit": "(dimensionless)",
                "points": 4,
            },
            {
                "label": "(e)",
                "text": (
                    "If an alien on Kappist a reports a light intensity of 5000 W/m², then "
                    "spontaneously teleports to Earth (which is 10 lightyears away from Kappist), "
                    "what light intensity would the alien report from Kappist now in **W/m²**?"
                ),
                "answer": 5e-8,
                "unit": "W/m²",
                "points": 2,
            },
            {
                "label": "(f)",
                "text": (
                    "Using Figure 1, if the peak emitted wavelength is actually 280 nanometers, "
                    "what is the **non-relativistic redshift**?"
                ),
                "answer": 0.07142857143,
                "unit": "(dimensionless)",
                "points": 2,
            },
            {
                "label": "(g)",
                "text": (
                    "From the perspective of someone on Earth, how fast is Kappist "
                    "moving away from them in **m/s**?"
                ),
                "answer": 0.2146,
                "unit": "m/s",
                "points": 2,
            },
        ],
    },
    {
        "number": 74,
        "title": "Planet Mirad a — Orbital Mechanics & Magnitudes",
        "intro": (
            "**Question 74 (28 points)**\n\n"
            "The planet **Mirad a** is orbiting **Mirad** in an elliptical orbit with an "
            "eccentricity of **0.19** and a period of **600 Earth days**. "
            "The absolute magnitude of Mirad is **5.76**. "
            "The radius and mass of Mirad are **0.95 R☉** and **0.8 M☉**, respectively, "
            "and the radius and mass of Mirad a are **1.2 R_Earth** and **1.5 M_Earth**."
        ),
        "figure": None,
        "parts": [
            {
                "label": "(a)",
                "text": "What is the length of the **semi-major axis** (in **AU**)?",
                "answer": 1.29,
                "unit": "AU",
                "points": 2,
            },
            {
                "label": "(b)",
                "text": "What is the length of the **semi-minor axis** (in **AU**)?",
                "answer": 1.27,
                "unit": "AU",
                "points": 2,
            },
            {
                "label": "(c)",
                "text": (
                    "What is the **potential energy** of the orbit when the distance between "
                    "Mirad a and Mirad is equal to the distance of the semi-major axis in **Joules**?"
                ),
                "answer": 4.925e33,
                "unit": "J",
                "points": 4,
            },
            {
                "label": "(d)",
                "text": "What is the **velocity** of Mirad a at the **perihelion** in **m/s**?",
                "answer": 28424.68,
                "unit": "m/s",
                "points": 2,
            },
            {
                "label": "(e)",
                "text": "What is the **velocity** of Mirad a at the **aphelion** in **m/s**?",
                "answer": 19347.89,
                "unit": "m/s",
                "points": 2,
            },
            {
                "label": "(f)",
                "text": (
                    "How fast would an object need to move to **escape the atmosphere** "
                    "of Mirad a in **m/s**?"
                ),
                "answer": 12493.319,
                "unit": "m/s",
                "points": 4,
            },
            {
                "label": "(g)",
                "text": (
                    "From Earth, the angular diameter of Mirad is **0.007 degrees**. "
                    "What is the **distance** from Earth to Mirad in **AU**?"
                ),
                "answer": 72.32,
                "unit": "AU",
                "points": 4,
            },
            {
                "label": "(h)",
                "text": "What is the **distance modulus** of Mirad from Earth?",
                "answer": -22.3,
                "unit": "(dimensionless)",
                "points": 4,
            },
            {
                "label": "(i)",
                "text": "Calculate the **apparent magnitude** of Mirad.",
                "answer": -16.54,
                "unit": "(dimensionless)",
                "points": 4,
            },
        ],
    },
    {
        "number": 75,
        "title": "Binary Stars Zenor I & II — Radial Velocity",
        "intro": (
            "**Question 75 (18 points)**\n\n"
            "Two stars **Zenor I** and **Zenor II** are orbiting each other, "
            "with the radial velocity graph as shown in Figure 2."
        ),
        "figure": "images/fig2_zenor_radial_velocity.png",
        "parts": [
            {
                "label": "(a)",
                "text": "Calculate the **separation** between the two stars in **AU**.",
                "answer": 0.160857,
                "unit": "AU",
                "points": 2,
            },
            {
                "label": "(b)",
                "text": "Find the **ratio** of the mass of Zenor I to the mass of Zenor II.",
                "answer": 1.5,
                "unit": "(dimensionless)",
                "points": 2,
            },
            {
                "label": "(c)",
                "text": "Find the **sum of the masses** of Zenor I and Zenor II in **M☉**.",
                "answer": 11.316,
                "unit": "M☉",
                "points": 4,
            },
            {
                "label": "(d)",
                "text": "Find the **mass of Zenor I** in **M☉**.",
                "answer": 6.79,
                "unit": "M☉",
                "points": 4,
            },
            {
                "label": "(e)",
                "text": "Find the **mass of Zenor II** in **M☉**.",
                "answer": 4.53,
                "unit": "M☉",
                "points": 4,
            },
            {
                "label": "(f)",
                "text": (
                    "Calculate the **gravitational force** between these two stars in **Newtons**."
                ),
                "answer": 1.52e31,
                "unit": "N",
                "points": 2,
            },
        ],
    },
    {
        "number": 76,
        "title": "Transit of Spectris a — Flux Ratio & Geometry",
        "intro": (
            "**Question 76 (16 points)**\n\n"
            "Figure 3 and Figure 4 show two scales of the same graph measuring the flux "
            "ratio of a transit of planet **Spectris a** in orbit with the star **Spectris**. "
            "The radius and mass of Spectris are observed to be similar to the Sun."
        ),
        "figure": "images/fig3_spectris_transit_days.png",
        "figure2": "images/fig4_spectris_transit_minutes.png",
        "parts": [
            {
                "label": "(a)",
                "text": "What **fraction** of Spectris a's orbit is in transit of Spectris?",
                "answer": 9.259259e-4,
                "unit": "(dimensionless)",
                "points": 2,
            },
            {
                "label": "(b)",
                "text": (
                    "Using Kepler's Third Law, and approximating "
                    "M_Spectris + M_Spectris_a ≈ M_Spectris, and assuming a circular orbit, "
                    "calculate the **separation** between Spectris a and Spectris in **AU**."
                ),
                "answer": 0.0257,
                "unit": "AU",
                "points": 6,
            },
            {
                "label": "(c)",
                "text": (
                    "Calculate the approximate **distance traveled** by Spectris a during its "
                    "transit, assuming that from our view on Earth, Spectris a crosses the center "
                    "of Spectris in the middle of the transit. Answer in **R_Earth**."
                ),
                "answer": 3.5,
                "unit": "R_Earth",
                "points": 4,
            },
            {
                "label": "(d)",
                "text": (
                    "The calendar of the hypothetical inhabitants of Spectris a consists of "
                    "seventeen months. Imagining a straight line connecting the planet and the "
                    "star, what is the **area swept out** by this line in five Spectris a months "
                    "in **m²**?"
                ),
                "answer": 1.365e19,
                "unit": "m²",
                "points": 4,
            },
        ],
    },
]
