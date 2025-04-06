```markdown
# 🏎️ Hand Gesture-Controlled Hill Climb Racing 🎮

Control the popular game **Hill Climb Racing** using just your hand gestures!  
This project uses **Python**, **OpenCV**, and **MediaPipe** to detect hand gestures in real-time and simulate key presses for game control. No mouse or keyboard—just wave your hands to race! 🖐️🚀

---

## ✨ Features

- 🖐️ **Open Hand** → Accelerate (Right Arrow Key)
- ✊ **Closed Fist** → Brake (Left Arrow Key)
- 🤖 Real-time hand tracking with **MediaPipe**
- 🧠 Continuous key holding while gesture is detected
- 🎮 Seamless control over gameplay
- 🪟 Automatically focuses Hill Climb Racing window

---

## 🛠️ Tech Stack

- **Python 3.x**
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- `pynput` for simulating keypresses
- `pywin32` for bringing game window to focus

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/hill-climb-gesture-controller.git
cd hill-climb-gesture-controller
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install additional packages if not already installed**

```bash
pip install opencv-python mediapipe pynput pywin32
```

---

## 🧠 Usage

1. Open **Hill Climb Racing** manually (e.g., from Microsoft Store)
2. Run the main script:

```bash
python main.py
```

3. Use your hand in front of your webcam:
   - ✋ Show an **open hand** to **accelerate**
   - ✊ Show a **closed fist** to **brake**
   - Remove your hand or change the gesture to release the keys

4. Press `Q` to quit the controller.

---

## 📁 Project Structure

```
hill-climb-gesture-controller/
│
├── main.py                # Main script to start the controller
├── gesture_utils.py       # Gesture detection logic using MediaPipe
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

---

## 🎯 Future Enhancements

- Add more gestures (e.g., thumbs-up to restart)
- Custom gesture training
- GUI overlay showing current gesture & FPS
- Voice feedback and calibration options

---

## 🧑‍💻 Author

**Ujesh**  
Passionate about AI, automation, and innovative game control systems!

---

## 🔗 Connect

Feel free to share your thoughts, suggestions, or feedback!

---

## 🏷️ Hashtags

```
#Python #OpenCV #MediaPipe #ComputerVision #GestureControl #HillClimbRacing #GamingAI #AIProjects #Automation #TechInnovation
