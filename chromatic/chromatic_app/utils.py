from django.conf import settings

import cv2
import numpy as np

def get_faces(image_path):
    image_path = str(settings.MEDIA_ROOT / str(image_path))
    img = cv2.imread(image_path)

    return get_faces_helper(img)

def get_faces_helper(img):
    face_cascade = cv2.CascadeClassifier(str(settings.BASE_DIR / 'haarcascade_frontalface_default.xml'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if isinstance(faces, np.ndarray):
        for i in range(faces.shape[0]):
            faces[i][0] = int((faces[i][0] / gray.shape[1]) * 100)
            faces[i][1] = int((faces[i][1] / gray.shape[0]) * 100)
            faces[i][2] = int((faces[i][2] / gray.shape[1]) * 100)
            faces[i][3] = int((faces[i][3] / gray.shape[0]) * 100)

    return faces