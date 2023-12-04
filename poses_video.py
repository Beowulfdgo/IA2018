import cv2
import mediapipe as mp
from tkinter import Tk, filedialog

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename()
cap = cv2.VideoCapture(image_path)

with mp_pose.Pose(
    static_image_mode=False) as pose:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break 
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
        results = pose.process (frame_rgb)

        if results.pose_landmarks is not None:
            mp_drawing.draw_landmarks (
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
                mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3), 
                mp_drawing.DrawingSpec(color=(255, 255, 250), thickness=2))
            
        cv2.imshow("Frame", frame) 
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release ()
cv2.destroyAllWindows ()