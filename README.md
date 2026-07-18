# 🎵 Music Recommender Simulation

## Project Summary

This project implements **VibeFinder**, a content-based music recommendation system built in Python. The system compares the musical characteristics of songs with a user's listening preferences, calculates a weighted compatibility score, and recommends the highest-ranked songs. Users can choose between multiple ranking strategies, including Balanced, Genre First, Mood First, and Energy Similarity, to see how different scoring priorities change the recommendations. The project demonstrates how recommendation systems transform structured data into personalized predictions while also highlighting the importance of feature engineering, ranking algorithms, and transparency.

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

Loaded songs: 20

Choose a ranking mode:
1. Balanced
2. Genre First
3. Mood First
4. Energy Similarity
Enter 1, 2, 3, or 4: 1

====================================================================================================
Profile: High-Energy Pop Fan
Ranking mode: balanced
====================================================================================================
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Rank | Song              | Artist        | Genre     | Mood     |   Score | Reasons                                                                                                                                                                                                                                     |
+========+===================+===============+===========+==========+=========+=============================================================================================================================================================================================================================================+
|      1 | City Lights Again | Metro Bloom   | pop       | happy    |   11.07 | genre match (+2.0); mood match (+1.5); energy similarity (+1.86); tempo similarity (+0.96); danceability similarity (+0.97); acousticness similarity (+0.94); valence similarity (+0.98); preferred decade (+1.0); popularity match (+0.86) |
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      2 | Sunrise City      | Neon Echo     | pop       | happy    |   11.02 | genre match (+2.0); mood match (+1.5); energy similarity (+1.88); tempo similarity (+0.93); danceability similarity (+0.91); acousticness similarity (+0.97); valence similarity (+0.99); preferred decade (+1.0); popularity match (+0.84) |
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      3 | Gym Hero          | Max Pulse     | pop       | intense  |    9.55 | genre match (+2.0); energy similarity (+1.90); tempo similarity (+0.93); danceability similarity (+1.00); acousticness similarity (+0.90); valence similarity (+0.92); preferred decade (+1.0); popularity match (+0.90)                    |
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      4 | Rooftop Lights    | Indigo Parade | indie pop | happy    |    7.76 | mood match (+1.5); energy similarity (+1.76); tempo similarity (+0.99); danceability similarity (+0.94); acousticness similarity (+0.80); valence similarity (+0.96); popularity match (+0.81)                                              |
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      5 | Neon Heartbeat    | Pixel Hearts  | synthwave | euphoric |    7.71 | energy similarity (+1.92); tempo similarity (+0.99); danceability similarity (+0.99); acousticness similarity (+0.99); valence similarity (+0.99); preferred decade (+1.0); popularity match (+0.83)                                        |
+--------+-------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

====================================================================================================
Profile: Chill Lofi Listener
Ranking mode: balanced
====================================================================================================
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Rank | Song               | Artist         | Genre   | Mood    |   Score | Reasons                                                                                                                                                                                                                                                                                     |
+========+====================+================+=========+=========+=========+=============================================================================================================================================================================================================================================================================================+
|      1 | Library Rain       | Paper Lanterns | lofi    | chill   |   11.98 | genre match (+2.0); mood match (+1.5); energy similarity (+2.00); tempo similarity (+0.97); danceability similarity (+0.97); acousticness similarity (+0.96); valence similarity (+0.98); instrumentalness similarity (+0.99); preferred decade (+1.0); popularity match (+0.61)            |
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      2 | Midnight Coding    | LoRoom         | lofi    | chill   |   11.73 | genre match (+2.0); mood match (+1.5); energy similarity (+1.86); tempo similarity (+0.97); danceability similarity (+0.93); acousticness similarity (+0.89); valence similarity (+0.98); instrumentalness similarity (+0.92); preferred decade (+1.0); popularity match (+0.68)            |
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      3 | Focus Flow         | LoRoom         | lofi    | focused |    8.94 | genre match (+2.0); energy similarity (+1.90); tempo similarity (+0.95); danceability similarity (+0.95); acousticness similarity (+0.96); valence similarity (+0.99); instrumentalness similarity (+0.96); preferred decade (+1.0); popularity match (+0.73); repeat artist penalty (-1.5) |
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      4 | Spacewalk Thoughts | Orbit Bloom    | ambient | chill   |    8.31 | mood match (+1.5); energy similarity (+1.86); tempo similarity (+0.85); danceability similarity (+0.86); acousticness similarity (+0.90); valence similarity (+0.93); instrumentalness similarity (+0.86); popularity match (+0.55)                                                         |
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      5 | Deep Work Mode     | Signal Drift   | ambient | focused |    8.18 | energy similarity (+1.98); tempo similarity (+0.95); danceability similarity (+0.85); acousticness similarity (+0.94); valence similarity (+1.00); instrumentalness similarity (+0.89); preferred decade (+1.0); popularity match (+0.57)                                                   |
+--------+--------------------+----------------+---------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

====================================================================================================
Profile: Intense Rock Listener
Ranking mode: balanced
====================================================================================================
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Rank | Song             | Artist        | Genre     | Mood     |   Score | Reasons                                                                                                                                                                                                                                     |
+========+==================+===============+===========+==========+=========+=============================================================================================================================================================================================================================================+
|      1 | Storm Runner     | Voltline      | rock      | intense  |   11.16 | genre match (+2.0); mood match (+1.5); energy similarity (+1.96); tempo similarity (+0.98); danceability similarity (+0.99); acousticness similarity (+1.00); valence similarity (+0.97); preferred decade (+1.0); popularity match (+0.76) |
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      2 | Desert Thunder   | Iron Mesa     | rock      | intense  |   10.08 | genre match (+2.0); mood match (+1.5); energy similarity (+1.92); tempo similarity (+0.96); danceability similarity (+0.98); acousticness similarity (+0.98); valence similarity (+0.99); popularity match (+0.75)                          |
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      3 | Gym Hero         | Max Pulse     | pop       | intense  |    7.62 | mood match (+1.5); energy similarity (+2.00); tempo similarity (+0.82); danceability similarity (+0.77); acousticness similarity (+0.95); valence similarity (+0.68); popularity match (+0.90)                                              |
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      4 | Rooftop Lights   | Indigo Parade | indie pop | happy    |    6.43 | energy similarity (+1.66); tempo similarity (+0.74); danceability similarity (+0.83); acousticness similarity (+0.75); valence similarity (+0.64); preferred decade (+1.0); popularity match (+0.81)                                        |
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      5 | Electric Skyline | Nova Rush     | edm       | euphoric |    5.95 | energy similarity (+1.94); tempo similarity (+0.88); danceability similarity (+0.74); acousticness similarity (+0.94); valence similarity (+0.57); popularity match (+0.88)                                                                 |
+--------+------------------+---------------+-----------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
---

## Experiments You Tried

During development, I experimented with several versions of the scoring algorithm.

### Experiment 1: Genre Weight

I reduced the genre weight from 2.0 to 0.5. The recommender became much less focused on matching the user's favorite genre, and songs from unrelated genres appeared more frequently near the top of the rankings.

### Experiment 2: Additional Features

I added popularity, release decade, instrumentalness, and speechiness to the scoring function. These additional features produced more personalized recommendations and allowed different user profiles to receive more distinct results.

### Experiment 3: Artist Diversity

I added an artist repetition penalty. Before this change, the recommender sometimes recommended multiple songs from the same artist. After adding the penalty, the recommendation list became noticeably more diverse while still maintaining high overall scores.

### Experiment 4: Ranking Modes

I implemented four different ranking modes (Balanced, Genre First, Mood First, and Energy Similarity). Running the same user profile under different modes showed that changing the feature weights significantly altered the recommendation order.

---

## Limitations and Risks

Although the recommender works well for this simulation, it has several limitations.

- The dataset only contains 20 songs, so recommendations are limited.
- The song attributes are manually created instead of collected from real music metadata.
- The recommender only uses content-based filtering and cannot learn from user behavior.
- The system may create a filter bubble by repeatedly recommending similar songs.
- Popularity can slightly favor mainstream songs over lesser-known artists.
- The scoring weights were manually chosen and may not represent every listener equally well.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:
## Reflection

This project helped me understand how recommendation systems transform structured data into personalized predictions. Before building the recommender, I assumed that systems like Spotify relied entirely on machine learning. Through this project, I learned that even a relatively simple weighted scoring algorithm can generate recommendations that feel personalized when meaningful song features are compared against user preferences.

I also learned that recommendation systems can unintentionally introduce bias through feature selection and scoring decisions. For example, giving genre or popularity too much weight can reduce diversity and repeatedly recommend similar music. Building multiple ranking modes and adding an artist diversity penalty demonstrated how small design choices can significantly change recommendation quality and fairness.



