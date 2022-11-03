import os
import cv2
from PIL import Image
from pyzbar.pyzbar import decode
from config import COUNTER


class Qread:
    def decode_img(self, files):
        global COUNTER
        try:
            decoded_obj = decode(Image.open(files))
            l = len(decoded_obj)
            if l > 0:
                for obj in decoded_obj:
                    COUNTER = True
                    return obj.data.decode('utf-8')
            else:
                return "Штрихкод не прочитался"
        except:
            return "Ошибка чтения штрихкода"




# decode_obj.data.decode('utf-8')






