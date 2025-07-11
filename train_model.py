import os
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Define dataset path
dataset_path = "dataset/train"
categories = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
img_size = 48  # FER2013 image size

X, y = [], []

# Check if dataset path exists
if not os.path.exists(dataset_path):
    raise ValueError(f"\U0001F6D1 Dataset path '{dataset_path}' does not exist! Check your folder structure.")

# Load dataset
for category in categories:
    folder_path = os.path.join(dataset_path, category)
    
    # Check if category folder exists
    if not os.path.exists(folder_path):
        print(f"⚠️ Warning: Category folder '{category}' not found! Skipping...")
        continue

    label = categories.index(category)
    
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            print(f"⚠️ Warning: Could not read image '{img_name}' in '{category}' folder!")
            continue
        
        img = cv2.resize(img, (img_size, img_size))
        X.append(img)
        y.append(label)

# Ensure data is loaded
if len(X) == 0 or len(y) == 0:
    raise ValueError("\U0001F6D1 No images were loaded! Check dataset structure and image formats.")

# Convert to NumPy arrays and normalize
X = np.array(X).reshape(-1, img_size, img_size, 1) / 255.0  # Normalize
y = to_categorical(np.array(y), num_classes=len(categories))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✅ Dataset Loaded! Total images: {len(X)}, Training: {len(X_train)}, Testing: {len(X_test)}")

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(categories), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the trained model
model_save_path = "models/emotion_model.h5"
os.makedirs("models", exist_ok=True)
model.save(model_save_path)
print(f"✅ Model training complete & saved at {model_save_path}!")
