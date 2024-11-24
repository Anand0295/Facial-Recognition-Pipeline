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