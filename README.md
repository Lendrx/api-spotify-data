# 🎵 Spotify API Projekt

Ein Python-basiertes Projekt zur Analyse von Spotify-Daten, das zeigt, wie die Spotify Web API genutzt werden kann, um interessante Einblicke in die Musikwelt zu gewinnen.

## 🎯 Projektziel

Dieses Projekt demonstriert die Verwendung der Spotify-API zur Datenextraktion und -analyse. Es dient als praktisches Beispiel für Entwickler:innen, die lernen möchten, wie man:
- Mit Web-APIs interagiert
- Daten strukturiert speichert und verarbeitet
- Musikdaten analysiert und visualisiert

## 🚀 Aktuelle Features

- **Künstlerdaten-Abruf**: Detaillierte Informationen zu Künstler:innen
- **Top-Tracks-Analyse**: Extraktion der populärsten Songs
- **Datenspeicherung**: Export in JSON und CSV Format
- **Basis-Datenanalyse**: Erste Auswertungen der gesammelten Daten

## 📋 Voraussetzungen

### Technische Requirements
- Python 3.10+
- Spotify Developer Account
- Git (für Versionskontrolle)

### Benötigte Python-Pakete
```python
requests
pandas
spotipy
python-dotenv
matplotlib
```

## ⚙️ Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/[username]/spotify-api-projekt.git
   cd spotify-api-projekt
   ```

2. **Abhängigkeiten installieren**
   ```bash
   pip install requests pandas spotipy python-dotenv matplotlib
   ```

3. **Umgebungsvariablen einrichten**
   ```env
   CLIENT_ID=deine_spotify_client_id
   CLIENT_SECRET=dein_spotify_client_secret
   ```

## 🎼 Spannende Erweiterungsmöglichkeiten

### 1. Audio-Feature-Analyse
```python
# Beispiel für Audio-Feature-Analyse
def get_audio_features(track_id):
    features = sp.audio_features(track_id)[0]
    return {
        'danceability': features['danceability'],
        'energy': features['energy'],
        'tempo': features['tempo'],
        'valence': features['valence']
    }
```
**Mögliche Erkenntnisse:**
- Tanzbarkeits-Score für verschiedene Genres
- Energie-Level-Vergleich zwischen Künstler:innen
- Tempo-Entwicklung über verschiedene Alben hinweg

### 2. Künstler-Collaboration-Netzwerk
```python
def analyze_collaborations(artist_id):
    # Finde alle Features des Künstlers
    features = sp.artist_top_tracks(artist_id)
    collaborators = set()
    for track in features:
        for artist in track['artists']:
            if artist['id'] != artist_id:
                collaborators.add(artist['name'])
    return collaborators
```
**Interessante Auswertungen:**
- Visualisierung des Kollaborations-Netzwerks
- Häufigste Zusammenarbeiten
- Genre-Überschneidungen bei Kollaborationen

### 3. Zeitliche Release-Analyse
```python
def analyze_release_pattern(artist_id):
    albums = sp.artist_albums(artist_id, album_type='album,single')
    releases = [{
        'name': album['name'],
        'date': album['release_date'],
        'type': album['album_type']
    } for album in albums['items']]
    return pd.DataFrame(releases)
```
**Mögliche Insights:**
- Optimale Release-Zeitpunkte
- Saisonale Trends
- Veröffentlichungsstrategien

### 4. Playlist-Erfolgsanalyse
```python
def analyze_playlist_success(playlist_id):
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']
    return [{
        'track': track['track']['name'],
        'popularity': track['track']['popularity'],
        'added_at': track['added_at']
    } for track in tracks]
```
**Spannende Auswertungen:**
- Korrelation zwischen Platzierung und Popularität
- Einfluss von Playlist-Features auf Streaming-Zahlen
- Genre-Mix erfolgreicher Playlists

### 5. Marktanalyse nach Regionen
```python
def analyze_market_presence(track_id):
    track = sp.track(track_id)
    markets = track['available_markets']
    return {
        'total_markets': len(markets),
        'regions': markets
    }
```
**Interessante Erkenntnisse:**
- Globale Verfügbarkeit von Tracks
- Regionale Popularitätsunterschiede
- Marktspezifische Release-Strategien

## 📊 Visualisierungsbeispiele

Das Projekt kann um folgende Visualisierungen erweitert werden:
- Heatmaps für Audio-Features
- Netzwerk-Graphen für Künstler-Kollaborationen
- Timeline-Plots für Release-Strategien
- Geographische Karten für Marktpräsenz
- Radar-Charts für Genre-Vergleiche

## 🛠️ Technische Erweiterungen

1. **Automatisierte Datenaktualisierung**
   ```python
   from apscheduler.schedulers.background import BackgroundScheduler
   scheduler = BackgroundScheduler()
   scheduler.add_job(update_data, 'interval', hours=24)
   ```

2. **Datenbank-Integration**
   ```python
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///spotify_data.db')
   df.to_sql('tracks', engine, if_exists='replace')
   ```

3. **API-Caching**
   ```python
   import functools
   @functools.lru_cache(maxsize=128)
   def cached_api_call(endpoint):
       return sp.api_call(endpoint)
   ```

## 📈 Mögliche Analysen

1. **Popularitätsprognosen**
   - Maschinelles Lernen zur Vorhersage von Track-Erfolg
   - Feature-Importance-Analyse
   - Trend-Prediction

2. **Genre-Evolution**
   - Tracking von Genre-Trends über Zeit
   - Subgenre-Entstehung und -Entwicklung
   - Cross-Genre-Einflüsse

3. **Künstler-Entwicklung**
   - Karriere-Trajectory-Analyse
   - Style-Evolution über Alben
   - Collaboration-Impact-Analyse

## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
