import os
import cv2
from mtcnn.mtcnn import MTCNN

def detect_face(image_path, output_folder):
    detector = MTCNN()
    image = cv2.imread(image_path)
    faces = detector.detect_faces(image)
    valid_faces = 0

    for face in faces:
        x, y, w, h = face['box']
        face_image = image[y:y+h, x:x+w]

        # Check aspect ratio for filtering valid faces
        face_aspect_ratio = float(w) / h
        if 0.75 < face_aspect_ratio < 1.33:
            unique_filename = f"face_{os.path.splitext(os.path.basename(image_path))[0]}_{valid_faces}.jpg"
            face_image_path = os.path.join(output_folder, unique_filename)
            cv2.imwrite(face_image_path, face_image)
            valid_faces += 1

# Reading theft images and detecting faces
theft_images_folder = "run-images"
output_folder = "face-images"
os.makedirs(output_folder, exist_ok=True)
for image_filename in os.listdir(theft_images_folder):
    image_path = os.path.join(theft_images_folder, image_filename)
    detect_face(image_path, output_folder)
