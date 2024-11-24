import cv2
import face_recognition

class FaceDetector:
    def detect(self, image_path):
        # Load and detect faces
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        return {
            'image': image,
            'locations': face_locations,
            'encodings': face_encodings
        }

face_detector.py
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

face_recognizer.py
import cv2

class Visualizer:
    def draw_results(self, image, faces):
        for face in faces:
            top, right, bottom, left = face['location']
            name = face['name']
            confidence = face['confidence']
            
            # Draw box
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Draw label
            label = f"{name} ({confidence:.0%})"
            cv2.putText(image, label, (left, top - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return image