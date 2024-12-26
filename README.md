# Spotify Data Explorer

## 🎯 Was macht es?
Analysesystem für Spotify-Daten mit Fokus auf Audio-Features und Hörgewohnheiten. Generiert detaillierte Insights aus Streaming-Daten.

## 🛠️ Wie ist es gebaut?
### Tech Stack:
- Python 3.x
- Spotipy
- FastAPI
- Pandas
- Redis

### Architektur-Highlights:
1. Asynchrone Datenverarbeitung
2. Audio-Feature-Analyse
3. Playlist-Pattern-Detection

## 📊 Technische Features
```python
async def analyze_playlist(playlist_id):
    tracks = await get_playlist_tracks(playlist_id)
    features = await get_audio_features(tracks)
    patterns = detect_music_patterns(features)
    return generate_playlist_insights(patterns)
```

Key Features:
- Audio-Pattern-Erkennung
- Playlist-Kategorisierung
- Feature-basierte Empfehlungen
