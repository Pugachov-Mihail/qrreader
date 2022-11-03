import os
import shutil
from PIL import Image
from pyzbar.pyzbar import decode
from .config import COUNTER


class Qread:
    qr = ''

    def decode_img(self, files, user):
        global COUNTER
        try:
            decoded_obj = decode(Image.open(files))
            l = len(decoded_obj)
            if l > 0:
                for obj in decoded_obj:
                    self.qr = obj.data.decode('utf-8')
                    COUNTER = True
                    self.delete_foldes(user)
                return self.qr
            else:
                COUNTER = True
                self.delete_foldes(user)
                return "Штрихкод не прочитался. " \
                       "Загрузи новое фото"
        except:
            return "Ошибка в чтении штрихкода"

    def delete_foldes(self, user):
        print(COUNTER)
        if COUNTER:
            try:
                os.chdir("application")
                print(os.getcwd())
                shutil.rmtree(f"{user}_img", ignore_errors=True)
                os.chdir("../")
            except:
                print(os.getcwd())

# decode_obj.data.decode('utf-8')
