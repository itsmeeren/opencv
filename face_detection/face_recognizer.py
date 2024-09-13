import cv2 as cv
import numpy as np
import os

# Creating the empty list for people
people = []
DIR = '/home/karthik/opencv/people/'

for person in os.listdir(DIR):
    if os.path.isdir(os.path.join(DIR, person)):  # Ensure it's a directory
        people.append(person)

print(f"People: {people}")

# Using haarcascade classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Creating lists for features and labels
features = []
labels = []

# Function for training
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # Ensure the file is a valid image
            if img.endswith('.jpg') or img.endswith('.png'):
                img_array = cv.imread(img_path)

                # Check if the image was loaded properly
                if img_array is None:
                    print(f"Image not loaded properly: {img_path}")
                    continue

                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

                # Detect faces
                faces_recog = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                for (x, y, w, h) in faces_recog:
                    faces_roi = gray[y:y+h, x:x+w]

                    if faces_roi.size > 0:
                        faces_roi_resized = cv.resize(faces_roi, (100, 100))  # Resize to 100x100
                        features.append(faces_roi_resized)
                        labels.append(label)

# Call the function to populate features and labels
create_train()

# Check the lengths of features and labels
print(f"Length of features list: {len(features)}")
print(f"Length of labels list: {len(labels)}")

# Ensure both features and labels are not empty
if len(features) > 0 and len(labels) > 0:
    features = np.array(features, dtype=np.uint8)  # Ensure the correct data type
    labels = np.array(labels, dtype=np.int32)  # Ensure labels are of integer type

    # Ensure proper shape for training
    features = features.reshape(len(features), 100, 100)  # All images should be 100x100

    # Create the face recognizer
    face_recognizer = cv.face.LBPHFaceRecognizer_create()  # Ensure using the correct method
    face_recognizer.train(features, labels)
    face_recognizer.save('face_recognizer.yml')
else:
    print("No features or labels found. Training cannot proceed.")
