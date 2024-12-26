# Spotify Data Explorer

## 🎵 Überblick
Tool zur Analyse von Spotify-Daten mit Fokus auf Audio-Features und persönliche Hörgewohnheiten. Die Spotify API bietet:

- Audio-Features (Tempo, Tanzbarkeit, Energie etc.)
- Persönliche Hörstatistiken
- Playlist-Analysen
- Künstler- und Track-Metadaten

## 🔧 Voraussetzungen
- Python 3.x
- Spotify Developer Account
- Client ID & Secret von Spotify

## 📊 Analysemöglichkeiten mit der Spotify API

### 1. Audio-Features
```python
# Beispiel: Audio-Features eines Tracks abrufen
features = sp.audio_features(track_id)[0]
```
Analysierbare Merkmale:
- Tanzbarkeit (0.0 bis 1.0)
- Energie (0.0 bis 1.0)
- Tempo (BPM)
- Stimmung/Valence (0.0 bis 1.0)
- Instrumentalität
- Akustik

### 2. Playlist-Analyse
```python
# Beispiel: Durchschnittliche Energie einer Playlist
async def analyze_playlist_energy(playlist_id):
    tracks = await get_playlist_tracks(playlist_id)
    features = await get_audio_features(tracks)
    return np.mean([track['energy'] for track in features])
```

### 3. Hörgewohnheiten
- Top-Tracks und -Künstler
- Genre-Verteilung
- Zeitliche Entwicklung des Musikgeschmacks

## 🚀 Hauptfunktionen

1. **Feature-Analyse**
   - Audio-Merkmale von Tracks
   - Vergleich mehrerer Songs
   - Genre-Muster

2. **Playlist-Insights**
   - Energie-Verlauf
   - Genre-Mix
   - Mood-Mapping

3. **Personalisierte Statistiken**
   - Hörgewohnheiten
   - Lieblings-Genres
   - Ähnlichkeitsanalysen

## 📌 API Limits
- 429 Requests/Minute für API-Calls
- Batch-Requests für Tracks (max. 100 pro Request)
