# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used ChatGPT, Calude and deepseek as an AI coding assistant to help extend the starter music recommender into a more advanced recommendation system. My goals included expanding the dataset, improving the recommendation algorithm, adding multiple ranking strategies, implementing an artist diversity penalty, improving the terminal output, and debugging the project until all tests passed.


**Prompts used:**


- "Expand my songs.csv file to include 20 unique songs with realistic features."
- "Design a weighted scoring function for a content-based music recommender."
- "Add multiple ranking modes such as Balanced, Genre First, Mood First, and Energy Similarity."
- "Implement an artist diversity penalty so duplicate artists appear less often."
- "Help debug my Python imports and make sure all pytest tests pass."

**What did the agent generate or change?**

The AI helped generate or improve:

- `songs.csv` by expanding it to 20 songs with additional metadata.
- `recommender.py` by creating the weighted scoring function, ranking logic, and multiple recommendation modes.
- `main.py` by adding multiple user profiles and formatted recommendation tables.
- Documentation for the README and Model Card.
- Debugging suggestions for package imports and project structure.

**What did you verify or fix manually?**
I manually reviewed every code change before accepting it. I verified that:

- The recommendation scores made logical sense.
- The recommendations changed appropriately for different user profiles.
- The artist diversity penalty behaved correctly.
- The application ran without errors using `python -m src.main`.
- All starter tests passed using `python -m pytest`.


---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

### Which design pattern did you use?

**Strategy Pattern**

### How did AI help you brainstorm or implement it?

Initially, the recommender used one fixed scoring algorithm. During development, ChatGPT suggested separating the scoring weights into different ranking strategies instead of writing multiple versions of the scoring function. This made the code easier to maintain while allowing users to switch between recommendation styles.

### How does the pattern appear in your final code?

The Strategy Pattern appears in the `score_song()` function. Different weight dictionaries (`balanced`, `genre_first`, `mood_first`, and `energy_similarity`) represent different recommendation strategies. The selected strategy is passed into the scoring function, which applies the appropriate weights without changing the rest of the recommendation algorithm.
