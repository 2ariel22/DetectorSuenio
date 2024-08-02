import cv2, math
class Frame():
    def __init__(self,widh,height,speaker):
        self.img = None
        self.width =widh
        self.height = height
        self.speaker =speaker


    def processFrame(self,image,face_mesh):
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
                #(int(top[0] * self.width), int(top[1] * self.height)),
                #(int(bottom[0] * self.width), int(bottom[1] * self.height)),
                #(0, 255, 0), 3)

            

                cv2.circle(image, (int(top[0] * self.width), int(top[1] * self.height)), 4, (0,0,255), -1)
                cv2.circle(image, (int(bottom[0] * self.width), int(bottom[1] * self.height)), 4, (0,0,255), -1)

                cv2.circle(image, (int(ojo_derecho_supe[0] * self.width), int(ojo_derecho_supe[1] * self.height)), 1, (255,0,0), -1)
                
                cv2.circle(image, (int(ojo_izquierdo_supe[0] * self.width), int(ojo_izquierdo_supe[1] * self.height)), 1, (255,0,0), -1)
                
                cv2.circle(image, (int(infe[0] * self.width), int(infe[1] * self.height)), 4, (255,0,0), -1)
                
                

                fuente = cv2.FONT_HERSHEY_SIMPLEX
                tamano_letra = 1
                angulo = round(math.degrees(math.atan2(bottom[1] - top[1], bottom[0] - top[0])))
                
                if angulo<=80 or angulo>=100:
                    cv2.putText(image,'ALERTA!',(25,65),fuente,tamano_letra,(10, 10, 255),thickness=1)
                    if self.speaker.getStateSpeaker():
                        self.speaker.hablar("Advertencia, puede estar sufiendo de cansancio")
                        self.speaker.setStateSpeaker(False)
                else:
                    self.speaker.setStateSpeaker(True)

                cv2.imshow("frame",image)