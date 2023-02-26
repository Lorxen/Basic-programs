# Face detection program using cv2

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Import the image with a face
img = cv2.imread('test.jpg')

# Change the color of the image to grey scale so cv2 can read it
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Face detection code and square draw
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# Show the image with a rectangle on the face
cv2.imshow('img', img)

# Keep showing the image until user close window
cv2.waitKey()

# Save the image with the face detection with another name
cv2.imwrite('result.jpg', img)
