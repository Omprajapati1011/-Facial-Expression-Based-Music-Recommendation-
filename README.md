# 🎵 Facial Expression-Based Music Recommendation System

This project is an **AI-driven music recommendation system** that detects facial expressions in real-time and plays music based on the detected emotion.

---

## 📌 Features

* 📷 **Real-Time Face Detection** — Uses OpenCV to detect your face via webcam.
* 😊 **Facial Expression Recognition** — Classifies emotions like happy, sad, angry, neutral, surprise, etc.
* 🎶 **Emotion-Based Music Playback** — Plays songs that match your mood, using your local music files.

---

## 📂 Dataset

### FER-2013 Facial Expression Dataset

* The system is trained using the [FER-2013 dataset](https://www.kaggle.com/datasets/msambare/fer2013).
* **Download:** [FER-2013 on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)
* Place the `fer2013.csv` file into the `dataset/` directory.

```
project_root/
└── dataset/
    └── fer2013.csv
```

**Note:** Make sure `dataset/` is listed in `.gitignore`.

---

## 🎵 Music Dataset (Local)

Organize your local songs by emotion.
**Example structure:**

```
project_root/
└── music/
    ├── happy/
    │   ├── song1.mp3
    │   ├── song2.mp3
    ├── sad/
    │   ├── song1.mp3
    │   ├── song2.mp3
    ├── angry/
    ├── neutral/
    ├── surprise/
    └── ...
```

The program will detect your emotion and play a random song from the corresponding folder.

---

## 🗂️ Project Structure

```
/-Facial-Expression-Based-Music-Recommendation-/
│
├── dataset/               # FER-2013 CSV dataset
├── music/                 # Local music organized by emotion
├── models/                # Saved models & checkpoints
├── src/                   # Source code
│   ├── detect_face.py
│   ├── detect_emotion.py
│   ├── play_music.py
│   ├── main.py
│   └── ...
├── requirements.txt       # Project dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1️⃣ **Clone this repo**

```bash
git clone https://github.com/Omprajapati1011/-Facial-Expression-Based-Music-Recommendation-.git
cd -Facial-Expression-Based-Music-Recommendation-
```

2️⃣ **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1️⃣ Make sure your webcam works.

2️⃣ Run the main script:

```bash
python src/main.py
```

3️⃣ The webcam will detect your face, classify your emotion, and play a random song that matches your mood! 🎉

---

## ⚡ Dependencies

* OpenCV
* TensorFlow
* Keras
* NumPy
* Pygame (or similar for audio playback)

---

## 📃 .gitignore

Make sure you don’t push large files:

```
dataset/
music/
__pycache__/
*.pyc
venv/
```

---

## ✨ Credits

* **Dataset:** [FER-2013](https://www.kaggle.com/datasets/msambare/fer2013)
* **Libraries:** OpenCV, TensorFlow, Keras

---

## 📜 License

This project is for educational and research purposes only.

---

**Happy Coding! 😊🎵**
