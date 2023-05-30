import mediapipe as mp
import cv2, math, pyttsx3
aux_voz=True
def hablar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # Establece la voz en español latinoamericano
    engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz a 150 palabras por minuto
    engine.setProperty('volume', 1.0)  # Establece el volumen en 1.0 (máximo)
    engine.setProperty('pitch', 50)  # Ajusta el tono de la voz a 50 (más bajo)
    engine.say(texto)  # Mensaje a reproducir
    engine.runAndWait() 
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

                        ojo_derecho_supe =(face_landmarks.landmark[159].x, face_landmarks.landmark[159].y)
                        infe = (face_landmarks.landmark[1].x, face_landmarks.landmark[1].y)

                        ojo_izquierdo_supe =(face_landmarks.landmark[386].x, face_landmarks.landmark[386].y)
                        

                    

                        #cv2.line(
                        #image, 
                        #(int(top[0] * width), int(top[1] * height)),
                        #(int(bottom[0] * width), int(bottom[1] * height)),
                        #(0, 255, 0), 3)

                      

                        cv2.circle(image, (int(top[0] * width), int(top[1] * height)), 4, (0,0,255), -1)
                        cv2.circle(image, (int(bottom[0] * width), int(bottom[1] * height)), 4, (0,0,255), -1)

                        cv2.circle(image, (int(ojo_derecho_supe[0] * width), int(ojo_derecho_supe[1] * height)), 1, (255,0,0), -1)
                        
                        cv2.circle(image, (int(ojo_izquierdo_supe[0] * width), int(ojo_izquierdo_supe[1] * height)), 1, (255,0,0), -1)
                        
                        cv2.circle(image, (int(infe[0] * width), int(infe[1] * height)), 4, (255,0,0), -1)
                        


                        fuente = cv2.FONT_HERSHEY_SIMPLEX
                        tamano_letra = 1
                        angulo = round(math.degrees(math.atan2(bottom[1] - top[1], bottom[0] - top[0])))
                        
                        if angulo<=80 or angulo>=100:
                            cv2.putText(image,'ALERTA!',(25,65),fuente,tamano_letra,(10, 10, 255),thickness=1)
                            if aux_voz:
                                hablar("Advertencia, puede estar sufiendo de cansancio")
                                aux_voz=False
                        else:
                             aux_voz=True
                        
                       
                        
                cv2.imshow("frame",image)
                k = cv2.waitKey(1) & 0xFF
                if k==27:
                      break
cap.release()
cv2.destroyAllWindows()