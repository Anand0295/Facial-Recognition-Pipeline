from pipeline import FaceRecognitionSystem
import cv2

def main():
    # Initialize system
    system = FaceRecognitionSystem()
    
    # Add people to recognize
    system.add_person("data/person1.jpg", "John")
    system.add_person("data/person2.jpg", "Jane")
    
    # Process test image
    results, marked_image = system.process_image("data/test.jpg")
    
    # Save result
    cv2.imwrite("data/result.jpg", marked_image)

    # Print results
    for face in results:
        print(f"Found {face['name']} with {face['confidence']:.0%} confidence")

if __name__ == "__main__":
    main()