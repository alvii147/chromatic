from django.test import TestCase
from django.test import SimpleTestCase

import cv2
import urllib.request
import numpy as np

from ..utils import get_faces_helper

class TestUtils(TestCase):
    def test_get_faces(self):
        req = urllib.request.urlopen('https://source.unsplash.com/1600x900/?people')
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)

        faces = get_faces_helper(img)

        if isinstance(faces, tuple):
            self.assertEquals(len(faces), 0)
        else:
            self.assertIsInstance(faces, np.ndarray)
            self.assertEquals(faces.shape[-1], 4)