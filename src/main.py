from tabulate import tabulate

from src.recommender import load_songs, recommend_songs


def display_recommendations(
    profile_name: str,
    user_prefs: dict,
    songs: list,
    mode: str,
) -> None:
    """Display ranked recommendations in a readable table."""

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5,
        mode=mode,
    )

    print("\n" + "=" * 100)
    print(f"Profile: {profile_name}")
    print(f"Ranking mode: {mode}")
    print("=" * 100)

    table_rows = []

    for rank, recommendation in enumerate(recommendations, start=1):
        song = recommendation["song"]
        reasons = "; ".join(recommendation["reasons"])

        table_rows.append(
            [
                rank,
                song["title"],
                song["artist"],
                song["genre"],
                song["mood"],
                recommendation["score"],
                reasons,
            ]
        )

    headers = [
        "Rank",
        "Song",
        "Artist",
        "Genre",
        "Mood",
        "Score",
        "Reasons",
    ]

    print(
        tabulate(
            table_rows,
            headers=headers,
            tablefmt="grid",
        )
    )


def main() -> None:
    """Load songs and run the recommender for multiple profiles."""

    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop Fan": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.88,
            "target_tempo": 125,
            "target_danceability": 0.88,
            "target_valence": 0.85,
            "target_acousticness": 0.15,
            "preferred_decade": 2020,
            "minimum_popularity": 75,
        },
        "Chill Lofi Listener": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "target_tempo": 75,
            "target_danceability": 0.55,
            "target_valence": 0.58,
            "target_acousticness": 0.82,
            "target_instrumentalness": 0.80,
            "preferred_decade": 2020,
            "minimum_popularity": 50,
        },
        "Intense Rock Listener": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.93,
            "target_tempo": 150,
            "target_danceability": 0.65,
            "target_valence": 0.45,
            "target_acousticness": 0.10,
            "preferred_decade": 2010,
            "minimum_popularity": 65,
        },
    }

    available_modes = {
        "1": "balanced",
        "2": "genre_first",
        "3": "mood_first",
        "4": "energy_similarity",
    }

    print("\nChoose a ranking mode:")
    print("1. Balanced")
    print("2. Genre First")
    print("3. Mood First")
    print("4. Energy Similarity")

    selection = input("Enter 1, 2, 3, or 4: ").strip()
    mode = available_modes.get(selection, "balanced")

    if selection not in available_modes:
        print("Invalid choice. Using balanced mode.")

    for profile_name, user_prefs in profiles.items():
        display_recommendations(
            profile_name,
            user_prefs,
            songs,
            mode,
        )


if __name__ == "__main__":
    main()