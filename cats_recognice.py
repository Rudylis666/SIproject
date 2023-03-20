import cv2
import numpy as np
import sys

# Get user supplied values
cascPath = "cascade_cats8/cascade.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("cascade_cats8/cascade.xml")
cascade2=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

# Read the image
info = ["dog.8.jpg","cat.1000.jpg", "cat.1060.jpg", "cat.1002.jpg", "cat.1003.jpg", "cat.1004.jpg", "cat.1005.jpg", "cat.1006.jpg",
        "cat.1007.jpg", "cat.1008.jpg", "cat.1009.jpg", "cat.1010.jpg", "cat.1076.jpg", "cat.1012.jpg", "cat.1013.jpg",
        "cat1.jpg","cat2.jpg","cat3.jpg","cat4.jpg","cat5.jpg","cat6.jpg","cat7.jpg","cat8.jpg","cat9.jpg",
        "cat.1014.jpg", "cat.1015.jpg", "cat.1067.jpg", "cat.1031.jpg", "cats_dogs1.jpg","cats_dogs2.jpg","cats_dogs3.jpg","dog.1006.jpg"]
#info=["cat1.jpg","cat2.jpg","cat3.jpg","cat4.jpg","cat5.jpg","cat6.jpg","cat7.jpg","cat8.jpg","cat9.jpg"]
for element in info:
    print("Wczytuje zdjecie")
    nazwa = "test/" + element
    image = cv2.imread(nazwa)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(24, 24),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("My cats faces:", image)
    cv2.waitKey(0)
    print("Wczytuje zdjecie")
    nazwa = "test/" + element
    image = cv2.imread(nazwa)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = cascade2.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(24, 24),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Cv2 faces:", image)
    cv2.waitKey(0)


rectangles = faceCascade.detectMultiScale(image)
print("Znaleziono {0} kotów!".format(len(rectangles)))

# Draw a rectangle around the faces
for (x, y, w, h) in rectangles:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found2", image)
cv2.waitKey(0)
