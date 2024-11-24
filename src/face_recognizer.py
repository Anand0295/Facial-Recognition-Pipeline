import face_recognition
import numpy as np

class FaceRecognizer:
    def __init__(self):
        self.known_faces = []
        self.known_names = []
    
    def add_face(self, encoding, name):
        self.known_faces.append(encoding)
        self.known_names.append(name)
    
    def recognize(self, face_encoding):
        matches = face_recognition.compare_faces(self.known_faces, face_encoding)
        
        if True in matches:
            match_index = matches.index(True)
            confidence = 1 - face_recognition.face_distance(
                [self.known_faces[match_index]], 
                face_encoding
            )[0]
            return self.known_names[match_index], confidence
            
        return "Unknown", 0.0