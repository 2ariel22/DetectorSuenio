import mediapipe as mp
import cv2
from Resource.Speaker import Speaker
from Resource.Frame import Frame

class FaceDetection():
    def __init__(self):            
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.cap = None
        self.frame = None
      
        
        

    def init(self):
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.frame = Frame(speaker=Speaker(),
                           widh=int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           height=int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    def detect(self):
        with self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.01,
            refine_landmarks=True) as face_mesh:
                while self.cap.isOpened():
                    success, image = self.cap.read()
                    if not success:
                        continue
        
                    self.frame.processFrame(image,face_mesh)
        
                    k = cv2.waitKey(1) & 0xFF
                    if k==27:
                        break
        self.cap.release()
        cv2.destroyAllWindows()