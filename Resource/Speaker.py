import pyttsx3
class Speaker():
    def __init__(self):
        self.stateSpeaker=True
        self.engine = self.configEngine()

    def getStateSpeaker(self):
        return self.stateSpeaker
    def setStateSpeaker(self,state: bool):
        self.stateSpeaker = state

    def configEngine(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Establece la voz en español latinoamericano
        engine.setProperty('rate', 150)  # Ajusta la velocidad de la voz a 150 palabras por minuto
        engine.setProperty('volume', 1.0)  # Establece el volumen en 1.0 (máximo)
        engine.setProperty('pitch', 50)  # Ajusta el tono de la voz a 50 (más bajo)
        return engine
    def hablar(self,texto):
        self.engine.say(texto)  # Mensaje a reproducir
        self.engine.runAndWait() 