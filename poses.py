import cv2
import mediapipe as mp
from tkinter import Tk, filedialog

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename()

with mp_pose.Pose(
    static_image_mode=True) as pose:
    image = cv2.imread(image_path)
    #image = cv2.imread("C:/Users/xioma/Downloads/image_0001.jpg")
    height, width, _ = image.shape  
    image_rgb = cv2.cvtColor (image, cv2.COLOR_BGR2RGB)

    results = pose.process (image_rgb)
    print("Pose landmarks:", results.pose_landmarks)

    if results.pose_landmarks is not None:

        '''  mp_drawing.draw_landmarks(image, results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3), 
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
        ''' 
        print(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x*width))

        #brazo derecho
        x1 = int(results.pose_landmarks.landmark[mp_pose. PoseLandmark.RIGHT_SHOULDER].x*width)
        y1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y*height)

        x2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x*width)
        y2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y*height)

        x3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x*width) 
        y3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y*height)

        #brazo izquierdo
        x4 = int(results.pose_landmarks.landmark[11].x*width)
        y4 = int(results.pose_landmarks.landmark[11].y*height)

        x5 = int(results.pose_landmarks.landmark[13].x*width)
        y5 = int(results.pose_landmarks.landmark[13].y*height)

        x6 = int(results.pose_landmarks.landmark[15].x*width) 
        y6 = int(results.pose_landmarks.landmark[15].y*height)

        #pierna derecha
        x7 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * width)
        y7 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * height)

        x8 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * width)
        y8 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * height)

        x9 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x * width)
        y9 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * height)

        #pierna izquierda
        x10 = int(results.pose_landmarks.landmark[23].x * width)
        y10 = int(results.pose_landmarks.landmark[23].y * height)

        x11 = int(results.pose_landmarks.landmark[25].x * width)
        y11 = int(results.pose_landmarks.landmark[25].y * height)

        x12 = int(results.pose_landmarks.landmark[27].x * width)
        y12 = int(results.pose_landmarks.landmark[27].y * height)
        #pie izquierdo
        x13 = int(results.pose_landmarks.landmark[29].x * width)
        y13 = int(results.pose_landmarks.landmark[29].y * height)

        x14 = int(results.pose_landmarks.landmark[31].x * width)
        y14 = int(results.pose_landmarks.landmark[31].y * height)
        #pie derecho
        x15 = int(results.pose_landmarks.landmark[32].x * width)
        y15 = int(results.pose_landmarks.landmark[32].y * height)

        x16 = int(results.pose_landmarks.landmark[30].x * width)
        y16 = int(results.pose_landmarks.landmark[30].y * height)

        #mano derecha
        x18 = int(results.pose_landmarks.landmark[18].x * width)
        y18 = int(results.pose_landmarks.landmark[18].y * height)
        
        x20 = int(results.pose_landmarks.landmark[20].x * width)
        y20 = int(results.pose_landmarks.landmark[20].y * height)

        x22 = int(results.pose_landmarks.landmark[22].x * width)
        y22 = int(results.pose_landmarks.landmark[22].y * height)
        #mano izquierda
        x17 = int(results.pose_landmarks.landmark[17].x * width)
        y17 = int(results.pose_landmarks.landmark[17].y * height)
        
        x19 = int(results.pose_landmarks.landmark[19].x * width)
        y19 = int(results.pose_landmarks.landmark[19].y * height)

        x21 = int(results.pose_landmarks.landmark[21].x * width)
        y21 = int(results.pose_landmarks.landmark[21].y * height)

        #lineas que unden el torzo
        cv2.line(image, (x1, y1), (x4, y4), (255, 255, 255), 3) 
        cv2.line(image, (x1, y1), (x7, y7), (255, 255, 255), 3) 
        cv2.line(image, (x4, y4), (x10, y10), (255, 255, 255), 3) 
        cv2.line(image, (x7, y7), (x10, y10), (255, 255, 255), 3)
        #pierna izquierda
        cv2.line(image, (x10, y10), (x11, y11), (255, 255, 255), 3) 
        cv2.line(image, (x11, y11), (x12, y12), (255, 255, 255), 3)
        cv2.line(image, (x13, y13), (x12, y12), (255, 255, 255), 3)
        cv2.line(image, (x14, y14), (x12, y12), (255, 255, 255), 3)
         
        cv2.circle(image, (x10, y10), 6, (255, 191, 0), -1) 
        cv2.circle(image, (x11, y11), 6, (255, 191, 0), -1)
        cv2.circle(image, (x12, y12), 6, (255, 191, 0),-1)
        #pie izquierdo
        cv2.line(image, (x13, y13), (x14, y14), (255, 255, 255), 3) 
    
        cv2.circle(image, (x13, y13), 6, (255, 191, 0), -1)
        cv2.circle(image, (x14, y14), 6, (255, 191, 0),-1)
        #pierna derecha
        cv2.line(image, (x7, y7), (x8, y8), (255, 255, 255), 3) 
        cv2.line(image, (x8, y8), (x9, y9), (255, 255, 255), 3)
        cv2.line(image, (x15, y15), (x9, y9), (255, 255, 255), 3)
        cv2.line(image, (x16, y16), (x9, y9), (255, 255, 255), 3)
        
        cv2.circle(image, (x7, y7), 6, (128, 0, 255), -1) 
        cv2.circle(image, (x8, y8), 6, (128,0, 255), -1)
        cv2.circle(image, (x9, y9), 6, (128, 0, 255),-1)
        #pie derecho
        cv2.line(image, (x15, y15), (x16, y16), (255, 255, 255), 3) 
    
        cv2.circle(image, (x15, y15), 6, (128, 0, 255), -1)
        cv2.circle(image, (x16, y16), 6, (128, 0, 255),-1)
        #brazo izquierdo
        cv2.line(image, (x4, y4), (x5, y5), (255, 255, 255), 3) 
        cv2.line(image, (x5, y5), (x6, y6), (255, 255, 255), 3) 
        cv2.line(image, (x6, y6), (x17, y17), (255, 255, 255), 3) 
        cv2.line(image, (x6, y6), (x19, y19), (255, 255, 255), 3) 
        cv2.line(image, (x6, y6), (x21, y21), (255, 255, 255), 3) 
        cv2.circle(image, (x4, y4), 6, (255, 191, 0), -1)
        cv2.circle(image, (x5, y5), 6, (255, 191, 0), -1)
        cv2.circle(image, (x6, y6), 6, (255, 191, 0), -1)

        #mano izquierda
        cv2.line(image, (x19, y19), (x17, y17), (255, 255, 255), 3) 
    
        cv2.circle(image, (x19, y19), 6, (255, 191, 0), -1)
        cv2.circle(image, (x17, y17), 6, (255, 191, 0),-1)
        cv2.circle(image, (x21, y21), 6, (255, 191, 0),-1)
        #brazo derecho
        cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), 3) 
        cv2.line(image, (x2, y2), (x3, y3), (255, 255, 255), 3) 
        cv2.line(image, (x18, y18), (x3, y3), (255, 255, 255), 3) 
        cv2.line(image, (x20, y20), (x3, y3), (255, 255, 255), 3) 
        cv2.line(image, (x22, y22), (x3, y3), (255, 255, 255), 3) 
        cv2.circle(image, (x1, y1), 6, (128, 0, 255), -1) 
        cv2.circle(image, (x2, y2), 6, (128,0, 255), -1)
        cv2.circle(image, (x3, y3), 6, (128, 0, 255),-1)
        #mano derecha
        cv2.line(image, (x18, y18), (x20, y20), (255, 255, 255), 3) 
    
        cv2.circle(image, (x18, y18), 6, (128, 0, 255), -1)
        cv2.circle(image, (x20, y20), 6, (128, 0, 255),-1)
        cv2.circle(image, (x22, y22), 6, (128, 0, 255),-1)

        
cv2.imshow ("Image", image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()