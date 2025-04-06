import cv2
import time
import win32gui
import win32con
from pynput.keyboard import Controller, Key
from gesture_utils import HandGesture

keyboard = Controller()

print("🕹️ Please open Hill Climb Racing manually now...")
time.sleep(5)

def focus_window(title_contains):
    def enumHandler(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            if title_contains.lower() in win32gui.GetWindowText(hwnd).lower():
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
    win32gui.EnumWindows(enumHandler, None)

focus_window("Hill Climb")

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
gesture_detector = HandGesture()

current_action = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    gesture, output_frame = gesture_detector.detect_gesture(frame)
    cv2.imshow("Gesture Controller", output_frame)

    if gesture == "open":
        if current_action != "accelerate":
            # Release brake if pressed
            keyboard.release(Key.left)
            # Press gas
            keyboard.press(Key.right)
            print("🚀 Holding Accelerate")
            current_action = "accelerate"

    elif gesture == "fist":
        if current_action != "brake":
            # Release gas if pressed
            keyboard.release(Key.right)
            # Press brake
            keyboard.press(Key.left)
            print("🛑 Holding Brake")
            current_action = "brake"

    else:
        # No hand detected or unknown gesture, release all
        if current_action is not None:
            keyboard.release(Key.right)
            keyboard.release(Key.left)
            print("🕳️ No gesture → Releasing all keys")
            current_action = None

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
