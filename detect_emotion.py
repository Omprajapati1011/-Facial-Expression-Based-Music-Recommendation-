
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

# Load trained model
model = load_model("models/emotion_model.h5")
categories = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Store last detected emotion
last_detected_emotion = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]  # Extract face region
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        face = cv2.resize(face, (48, 48))  # Resize to match model input
        face = np.expand_dims(face, axis=-1)  # Add channel dimension (shape: 48, 48, 1)
        face = np.expand_dims(face, axis=0)  # Add batch dimension (shape: 1, 48, 48, 1)
        face = face / 255.0  # Normalize pixel values

        # Make prediction
        prediction = model.predict(face)
        emotion = categories[np.argmax(prediction)]

        # Store the last detected emotion
        last_detected_emotion = emotion

        # Draw bounding box and emotion text
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)

    # Display frame
    cv2.imshow("Facial Emotion Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(f"🛑 Exiting... Last detected emotion: {last_detected_emotion}")
        break

cap.release()
cv2.destroyAllWindows()

# Return the last emotion for use in the recommendation script
print(f"Detected emotion: {last_detected_emotion}")
