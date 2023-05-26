import mediapipe as mp
import cv2 
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

with mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        min_detection_confidence=0.01,
        refine_landmarks=True) as face_mesh:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                      continue
                image.flags.writeable = False
                image = cv2.flip(image, 1)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                results = face_mesh.process(image)
    
                if results.multi_face_landmarks is not None:
                    for face_landmarks in results.multi_face_landmarks:

                        """image,
                        face_landmarks,
                        mp_face_mesh.FACEMESH_CONTOURS,
                        mp_drawing.DrawingSpec(color=(255,0,0),thickness=1,circle_radius=1),
                        mp_drawing.DrawingSpec(color=(150,150,150),thickness=1)"""
                        top = (face_landmarks.landmark[10].x, face_landmarks.landmark[10].y)
                        bottom = (face_landmarks.landmark[152].x, face_landmarks.landmark[152].y)
                    

                        cv2.line(
                        image, 
                        (int(top[0] * width), int(top[1] * height)),
                        (int(bottom[0] * width), int(bottom[1] * height)),
                        (0, 255, 0), 3
                        )

                        cv2.circle(image, (int(top[0] * width), int(top[1] * height)), 8, (0,0,255), -1)
                        cv2.circle(image, (int(bottom[0] * width), int(bottom[1] * height)), 8, (0,0,255), -1)
                        
                       
                        
                cv2.imshow("frame",image)
                k = cv2.waitKey(1) & 0xFF
                if k==27:
                      break
cap.release()
cv2.destroyAllWindows()