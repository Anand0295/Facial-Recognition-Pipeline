from .face_detector import FaceDetector
from .face_recognizer import FaceRecognizer
from .database_manager import Database
from .visualizer import Visualizer
import cv2

class FaceRecognitionSystem:
    def __init__(self):
        self.detector = FaceDetector()
        self.recognizer = FaceRecognizer()
        self.database = Database()
        self.visualizer = Visualizer()
        self._load_known_faces()
    
    def _load_known_faces(self):
        for encoding, name in self.database.get_all_faces():
            self.recognizer.add_face(encoding, name)
    
    def add_person(self, image_path, name):
        detection = self.detector.detect(image_path)
        if detection['encodings']:
            encoding = detection['encodings'][0]
            self.database.save(name, encoding)
            self.recognizer.add_face(encoding, name)
            return True
        return False
    
    def process_image(self, image_path):
        # Detect faces
        detection = self.detector.detect(image_path)
        
        results = []
        for encoding, location in zip(detection['encodings'], 
                                    detection['locations']):
            # Recognize each face
            name, confidence = self.recognizer.recognize(encoding)
            results.append({
                'name': name,
                'confidence': confidence,
                'location': location
            })
        
        # Draw results
        image = cv2.imread(image_path)
        marked_image = self.visualizer.draw_results(image, results)
        
        return results, marked_image