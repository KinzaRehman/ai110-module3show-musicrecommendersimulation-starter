# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---
## How The System Works

This project simulates a simple content-based music recommendation system. It compares the features of each song with a user's music preferences, calculates a score, and ranks the songs from strongest match to weakest match.

### Song Features

Each `Song` stores information that describes its musical style and sound. The features include:

- Genre
- Mood
- Energy
- Tempo in beats per minute
- Valence, which represents how positive or upbeat the song feels
- Danceability
- Acousticness
- Popularity
- Release decade
- Instrumentalness
- Speechiness

These features act as the input data used by the recommender.

### User Profile

Each `UserProfile` stores the listener's preferences. A profile can include:

- Favorite genre
- Favorite mood
- Target energy
- Target tempo
- Preferred danceability
- Preferred acousticness
- Preferred valence
- Preferred instrumentalness
- Preferred speechiness
- Preferred release decade
- Minimum popularity

The song data describes the music catalog, while the user profile describes what the listener is currently looking for.

### Scoring Songs

The recommender uses the `score_song()` function to compare one song with one user profile.

A song earns points when its genre or mood matches the user's favorites. It also earns similarity points when its energy, tempo, danceability, acousticness, and other numeric values are close to the user's target values.

For example, in balanced mode:

- A matching genre earns 2.0 points.
- A matching mood earns 1.5 points.
- Energy similarity can earn up to 2.0 points.
- Tempo similarity can earn up to 1.0 point.
- Other matching numeric attributes can add more points.
- A matching release decade can add 1.0 point.
- Popularity can add a small score when the song meets the user's minimum popularity preference.

The scoring function returns both a numeric score and a list of reasons, such as `genre match (+2.0)` or `energy similarity (+1.84)`. This makes the recommendations easier to understand.

### Ranking and Selecting Recommendations

The `recommend_songs()` function scores every song in the dataset. It then sorts the songs from highest score to lowest score and returns the top results.

The system also applies an artist repetition penalty when the same artist appears more than once. This encourages variety and reduces the chance that one artist dominates the recommendation list.

The user can choose between several ranking modes:

- Balanced
- Genre First
- Mood First
- Energy Similarity

Each mode changes the scoring weights, so the same user profile can receive different rankings depending on which musical feature is given the most importance.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



