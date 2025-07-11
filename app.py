import subprocess
import time
from recommend_music import play_last_emotion_music

# Run the emotion detection script
subprocess.run(["python", "detect_emotion.py"])

# Assume the last emotion detected is passed here. 
# For testing, we can use "Happy", but this should come from the emotion detected.
last_emotion = "Happy"  # You can dynamically update this with the last emotion detected

# Play the song based on the last detected emotion
play_last_emotion_music(last_emotion)

# Wait for a reasonable amount of time to let the music play
# You can adjust this time based on the length of the songs in your directory.
# Here, we assume 30 seconds as a placeholder.
time.sleep(30)  # Wait for the song to play for 30 seconds before exiting
