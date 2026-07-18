# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 is a content-based music recommendation system designed to recommend songs based on a listener's musical preferences. It compares song characteristics such as genre, mood, energy, tempo, and other musical features with a user's preferred listening style.

The recommender assumes that users know the type of music they currently enjoy and can describe their preferences through a set of attributes. This project is intended for educational purposes to demonstrate how recommendation systems work rather than for production use with real users.

---

## 3. How the Model Works

Each song is described using several musical features, including genre, mood, energy, tempo, danceability, acousticness, valence, popularity, release decade, instrumentalness, and speechiness.

Each user profile stores preferred values for many of these same features. The recommender compares every song against the user's preferences and assigns points whenever a song closely matches those preferences.

Songs receive additional points for matching the user's favorite genre and mood, while numerical features such as energy, tempo, and danceability earn similarity scores based on how close they are to the user's target values.

Unlike the starter project, I expanded the scoring algorithm to include additional song attributes, multiple ranking modes, and an artist diversity penalty that reduces repeated artists within the recommendation list.

---

## 4. Data

The recommender uses a manually created dataset containing **20 fictional songs**.

The dataset includes a variety of genres including:

- Pop
- Rock
- Lofi
- EDM
- Ambient
- Indie Pop
- Jazz
- Synthwave

Each song contains detailed metadata including musical characteristics and popularity values.

Although the dataset covers several musical styles, it is still relatively small and cannot represent the full diversity of real-world music.

---

## 5. Strengths

The recommender performs well when users have clearly defined musical preferences.

During testing:

- The High-Energy Pop profile consistently recommended energetic pop songs.
- The Chill Lofi profile correctly prioritized slower and more acoustic tracks.
- The Intense Rock profile selected energetic rock songs with matching moods.

The recommendation explanations also help users understand exactly why each song was recommended, making the system more transparent.

---

## 6. Limitations and Bias

The recommender has several limitations.

Because it only contains 20 songs, recommendations are naturally limited. Some genres have more representation than others, which can bias recommendations toward those genres.

The recommender only considers song metadata and does not learn from listening history, skipped songs, playlists, or user feedback.

Since the scoring weights were manually selected, different users may disagree with how important certain musical features should be.

Popularity also contributes slightly to the final score, which may unintentionally favor more popular songs over equally suitable lesser-known songs.

---

## 7. Evaluation

I evaluated the recommender using three different user profiles:

- High-Energy Pop Fan
- Chill Lofi Listener
- Intense Rock Listener

For each profile, I examined whether the highest-ranked songs matched the expected musical style and whether changing the ranking mode produced different recommendation orders.

I also verified that the artist diversity penalty reduced repeated artists while maintaining high-quality recommendations.

Finally, I ran the project's starter tests using `python -m pytest` to ensure that the implementation remained correct after adding new features.

---

## 8. Future Work

Future improvements could include:

- Expanding the catalog to thousands of real songs.
- Learning user preferences automatically from listening history.
- Incorporating lyrics and audio analysis.
- Supporting collaborative filtering using similar users.
- Adding feedback so recommendations improve over time.
- Increasing diversity by balancing genres and artists more intelligently.

---

## 9. Personal Reflection

This project helped me better understand how recommendation systems convert structured data into personalized suggestions. Before building the recommender, I assumed that systems like Spotify relied entirely on machine learning. I learned that carefully designed scoring algorithms can also produce meaningful recommendations.

One of the most interesting discoveries was seeing how small changes to feature weights dramatically changed the recommendation rankings. This reinforced how important feature engineering and ranking decisions are when designing AI systems and showed me that transparency is just as important as prediction accuracy.