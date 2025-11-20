import cv2, time, pyautogui
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# Configurations
SCROLL_SPEED = 600
SCROLL_DELAY = 0.5
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    # Check fingers (except thumb)
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)

    # Thumb detection
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if (handedness == "Right" and thumb_tip.x < thumb_ip.x) or \
       (handedness == "Left" and thumb_tip.x > thumb_ip.x):
        fingers.append(1)

    if sum(fingers) == 5:
        return "scroll_up"
    elif sum(fingers) == 0:
        return "scroll_down"
    else:
        return "none"


cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

last_scroll = p_time = 0

print("Gesture Scroll Control Active")
print("Open palm = Scroll Up")
print("Fist = Scroll Down")
print("Press 'q' to exit\n")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    gesture, handedness = "none", "unknown"

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand_landmarks, handedness)

            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if (time.time() - last_scroll) > SCROLL_DELAY:
                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                last_scroll = time.time()

    # FPS
    fps = 1 / (time.time() - p_time) if (time.time() - p_time) > 0 else 0
    p_time = time.time()

    cv2.putText(img, f'FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
