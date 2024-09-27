import cv2 as cv
import numpy as np
import os

# Load people's names
people = ['dhoni','ronaldo',"Kohli","messi",'mbappe']
# DIR = '/home/karthik/opencv/people/'
#
# for person in os.listdir(DIR):
#     if os.path.isdir(os.path.join(DIR, person)):
#         people.append(person)

# Load the trained face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_recognizer.yml')

# Load Haar Cascade for face detection
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Load the image for recognition
img = cv.imread('kohli.jpeg')
# img=img[20:200,100:400]
# cv.imshow(cropped)

# Convert the image to grayscale (required for face recognition)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

# Check if any faces were detected
if len(faces_rect) == 0:
    print("No faces detected in the image.")
else:
    # Iterate through the faces and make predictions
    for (x, y, w, h) in faces_rect:
        face_roi = gray[y:y+h, x:x+w]  # Extract the region of interest (the face)

        # Resize the face ROI to match the size used during training
        face_roi_resized = cv.resize(face_roi, (100, 100))  # Resize to 100x100 if that was the training size

        # Predict the label and confidence score
        label, confidence = face_recognizer.predict(face_roi_resized)

        # Check if the prediction is confident enough
        if confidence < 100:
            print(f'Label: {people[label]}, Confidence: {confidence:.2f}')
            # Annotate the image with the predicted label (person's name)
            cv.putText(img, people[label], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            print(f'Unknown face detected. Confidence: {confidence:.2f}')

        # Draw a rectangle around the detected face
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Showing  the detected image with the detected and recognized face
cv.imshow('Recognized Face', img)
cv.waitKey(0)
cv.destroyAllWindows()

