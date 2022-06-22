
import os
import cv2 as cv
import mouse
import winsound
import numpy as np
import mediapipe as mp
import time
import subprocess
def main():
    os.startfile('osk')
    subprocess.call(["cmd", "/c", "start", "/max", "C:\\Windows\\notepad.exe"])

a=True
mp_face_mesh = mp.solutions.face_mesh
LEFT_EYE =[362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
RIGHT_EYE=[33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
LEFT_IRIS = [474,475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]
cap = cv.VideoCapture(0)
a=True
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame,1)
        if not ret:
            break
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            # print(results.multi_face_landmarks[0].landmark)
            mesh_points=np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])
            (cx, cy), radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            #(r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            center_left = np.array([cx, cy], dtype=np.int32)
            if center_left[1]>250:
                #center_right = np.array([r_cx, r_cy], dtype=np.int32)
                cv.circle(frame, tuple(center_left), int(radius), (255,0,255), 1)
                #cv.circle(frame, tuple(center_right), int(r_radius), (255,0,255), 1)
                mask = np.zeros((img_h, img_w), dtype=np.uint8)
                cv.circle(mask, tuple(center_left), int(radius), (0,255,255), -1, cv.LINE_AA)
                cv.circle(frame, tuple(center_left), 1, (0,0,255), 1)
                #print("MASK",np.sum(mask))
                mouse.move(int(center_left[0]*3),int(center_left[1]*2.2))
            else:
                cv.putText(frame,"Please move your camera away from the keyboard",(100,100),1,1,(255,0,0))
        if a:
            main()
            a=False

        cv.imshow("Image",frame)
        key = cv.waitKey(10)
        if key == ord('q'):
          break
os.abort()
cap.release()
cv.destroyAllWindows()

