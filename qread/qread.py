import os
import cv2
from PIL import Image
from pyzbar.pyzbar import decode


class Qread:
    def decode(self):
        for i in self.files:
            decode_obj = decode(Image.open(i))
            for obj in decode_obj:
                return obj.data.decode('utf-8')

    def draw_barcode(self, decode, image):
        img = cv2.imread(image)
        print(img)
        return img



