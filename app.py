import face_recognition
import os

# Directory containing images of known individuals
known_faces_dir = "known_faces"
known_faces = []
known_names = []

# Load and encode known faces
for filename in os.listdir(known_faces_dir):
    image_path = os.path.join(known_faces_dir, filename)
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])