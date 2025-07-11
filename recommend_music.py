import os
import random
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Define emotion-to-music mapping
music_folder = "music/"
emotion_music = {
    "Angry": "angry/",
    "Happy": "happy/",
    "Sad": "sad/",
    "Neutral": "neutral/",
    "Surprise": "surprise/",
    "Fear": "fear/",
    "Disgust": "disgust/"
}

def play_music(emotion):
    folder = os.path.join(music_folder, emotion_music.get(emotion, "neutral"))

    # Check if the folder exists
    if not os.path.exists(folder):
        print(f"⚠️ Warning: Folder '{folder}' not found!")
        return

    # Get list of available songs
    songs = [f for f in os.listdir(folder) if f.endswith(('.mp3', '.wav'))]

    if not songs:
        print(f"⚠️ No songs found for '{emotion}' emotion!")
        return

    # Stop any currently playing music
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    # Select a random song
    song = random.choice(songs)
    song_path = os.path.join(folder, song)
    print(f"Attempting to play song: {song_path}")

    # Try loading and playing the song
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()  # Play the song once (not looping)
        print(f"🎵 Now Playing: {song}")
    except Exception as e:
        print(f"❌ Error playing song: {e}")

# Example usage: this will be triggered once 'q' is pressed in the webcam detection
def play_last_emotion_music(last_emotion):
    play_music(last_emotion)
