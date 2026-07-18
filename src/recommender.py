import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Song:
    """Represents a song and its musical attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    popularity: int = 0
    release_decade: int = 2020
    instrumentalness: float = 0.0
    speechiness: float = 0.0



@dataclass
class UserProfile:
    """Represents a user's music preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Object-oriented music recommendation system."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by preference score."""

        scored_songs = []

        for song in self.songs:
            score = 0.0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2.0

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.5

            score += max(0.0, 2.0 - abs(song.energy - user.target_energy) * 2)

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += 1.0 - song.acousticness

            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song,
    ) -> str:
        """Explain why a song matches the user's preferences."""

        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("matching genre")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("matching mood")

        energy_gap = abs(song.energy - user.target_energy)

        if energy_gap <= 0.10:
            reasons.append("very close energy level")
        elif energy_gap <= 0.25:
            reasons.append("similar energy level")

        if user.likes_acoustic and song.acousticness >= 0.60:
            reasons.append("strong acoustic sound")

        if not user.likes_acoustic and song.acousticness < 0.40:
            reasons.append("low acousticness")

        if not reasons:
            reasons.append("overall feature similarity")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""

    songs = []

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"].lower(),
                "mood": row["mood"].lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
                "popularity": int(row["popularity"]),
                "release_decade": int(row["release_decade"]),
                "instrumentalness": float(row["instrumentalness"]),
                "speechiness": float(row["speechiness"]),
            }

            songs.append(song)

    return songs


def score_song(
    user_prefs: Dict,
    song: Dict,
    mode: str = "balanced",
) -> Tuple[float, List[str]]:
    """Score one song using the selected ranking strategy."""

    score = 0.0
    reasons = []

    modes = {
        "balanced": {
            "genre": 2.0,
            "mood": 1.5,
            "energy": 2.0,
            "tempo": 1.0,
        },
        "genre_first": {
            "genre": 4.0,
            "mood": 1.0,
            "energy": 1.0,
            "tempo": 0.5,
        },
        "mood_first": {
            "genre": 1.0,
            "mood": 4.0,
            "energy": 1.5,
            "tempo": 0.5,
        },
        "energy_similarity": {
            "genre": 1.0,
            "mood": 1.0,
            "energy": 4.0,
            "tempo": 1.5,
        },
    }

    weights = modes.get(mode, modes["balanced"])

    favorite_genre = user_prefs.get("favorite_genre", "").lower()
    favorite_mood = user_prefs.get("favorite_mood", "").lower()

    if song["genre"].lower() == favorite_genre:
        score += weights["genre"]
        reasons.append(f"genre match (+{weights['genre']:.1f})")

    if song["mood"].lower() == favorite_mood:
        score += weights["mood"]
        reasons.append(f"mood match (+{weights['mood']:.1f})")

    target_energy = float(user_prefs.get("target_energy", 0.5))
    energy_gap = abs(song["energy"] - target_energy)
    energy_similarity = max(0.0, 1.0 - energy_gap)
    energy_score = energy_similarity * weights["energy"]

    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    target_tempo = float(
        user_prefs.get("target_tempo", song["tempo_bpm"])
    )
    tempo_gap = abs(song["tempo_bpm"] - target_tempo)
    tempo_similarity = max(0.0, 1.0 - tempo_gap / 100)
    tempo_score = tempo_similarity * weights["tempo"]

    score += tempo_score
    reasons.append(f"tempo similarity (+{tempo_score:.2f})")

    numeric_preferences = {
        "target_danceability": "danceability",
        "target_acousticness": "acousticness",
        "target_valence": "valence",
        "target_instrumentalness": "instrumentalness",
        "target_speechiness": "speechiness",
    }

    for preference_key, song_key in numeric_preferences.items():
        if preference_key in user_prefs:
            target_value = float(user_prefs[preference_key])
            difference = abs(song[song_key] - target_value)
            similarity_score = max(0.0, 1.0 - difference)

            score += similarity_score
            reasons.append(
                f"{song_key} similarity (+{similarity_score:.2f})"
            )

    if "preferred_decade" in user_prefs:
        preferred_decade = int(user_prefs["preferred_decade"])

        if song["release_decade"] == preferred_decade:
            score += 1.0
            reasons.append("preferred decade (+1.0)")

    if "minimum_popularity" in user_prefs:
        minimum_popularity = int(user_prefs["minimum_popularity"])

        if song["popularity"] >= minimum_popularity:
            popularity_score = song["popularity"] / 100
            score += popularity_score
            reasons.append(
                f"popularity match (+{popularity_score:.2f})"
            )

    return round(score, 2), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    mode: str = "balanced",
) -> List[Dict]:
    """Rank songs while encouraging artist diversity."""

    scored_songs = []

    for song in songs:
        score, reasons = score_song(
            user_prefs,
            song,
            mode=mode,
        )

        scored_songs.append(
            {
                "song": song,
                "score": score,
                "reasons": reasons,
            }
        )

    scored_songs.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True,
    )

    recommendations = []
    selected_artists = set()

    for recommendation in scored_songs:
        artist = recommendation["song"]["artist"]

        if artist in selected_artists:
            recommendation["score"] = round(
                recommendation["score"] - 1.5,
                2,
            )
            recommendation["reasons"].append(
                "repeat artist penalty (-1.5)"
            )

        recommendations.append(recommendation)
        selected_artists.add(artist)

    recommendations.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True,
    )

    return recommendations[:k]