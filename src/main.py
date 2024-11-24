from dotenv import load_dotenv
import os
import json
import base64
import pandas as pd
import matplotlib.pyplot as plt
from requests import post, get

# Laden der Umgebungsvariablen
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Pfad zum Speicherordner
DATA_FOLDER = "data"

def ensure_data_folder_exists():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        print(f"Ordner '{DATA_FOLDER}' wurde erstellt.")
    else:
        print(f"Ordner '{DATA_FOLDER}' ist bereits vorhanden.")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    
    if result.status_code != 200:
        print(f"Request failed: {result.status_code}")
        print(result.content)
        return None
    
    json_result = json.loads(result.content)
    if "artists" not in json_result:
        print("Key 'artists' not found in response")
        print(json_result)
        return None
    
    json_result = json_result["artists"]["items"]
    
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    if result.status_code != 200:
        print(f"Request failed: {result.status_code}")
        print(result.content)
        return None
    
    json_result = json.loads(result.content)["tracks"]
    return json_result

def save_to_csv(tracks):
    data = []
    for track in tracks:
        data.append({
            "Track Name": track["name"],
            "Album": track["album"]["name"],
            "Popularity": track["popularity"],
            "Spotify URL": track["external_urls"]["spotify"]
        })
    df = pd.DataFrame(data)
    filepath = os.path.join(DATA_FOLDER, "top_tracks.csv")
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

def save_to_json(tracks):
    data = []
    for track in tracks:
        data.append({
            "name": track["name"],
            "album": track["album"]["name"],
            "popularity": track["popularity"],
            "spotify_url": track["external_urls"]["spotify"]
        })
    filepath = os.path.join(DATA_FOLDER, "top_tracks.json")
    with open(filepath, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filepath}")

def visualize_tracks(tracks):
    track_names = [track["name"] for track in tracks]
    popularities = [track["popularity"] for track in tracks]

    plt.figure(figsize=(10, 6))
    plt.barh(track_names, popularities, color="skyblue")
    plt.xlabel("Popularity")
    plt.ylabel("Track Name")
    plt.title("Top Tracks by Popularity")
    plt.gca().invert_yaxis()  # Höchste Popularität oben
    plt.tight_layout()
    filepath = os.path.join(DATA_FOLDER, "popularity_chart.png")
    plt.savefig(filepath)
    plt.show()
    print(f"Visualization saved to {filepath}")

# Hauptprogramm
if __name__ == "__main__":
    ensure_data_folder_exists()
    token = get_token()
    artist_name = "Moksi"  # Beispiel-Artist
    result = search_for_artist(token, artist_name)

    if result:
        artist_id = result["id"]
        tracks = get_songs_by_artist(token, artist_id)
        
        if tracks:
            save_to_csv(tracks)
            save_to_json(tracks)
            visualize_tracks(tracks)
