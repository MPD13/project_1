import cv2

for i in range(5):  # Try indices 0 to 4
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Camera detected at index {i}")
        cap.release()
    else:
        print(f"❌ Cannot open camera at index {i}")
