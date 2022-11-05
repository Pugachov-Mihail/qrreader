from PIL import Image
from pyzbar.pyzbar import decode


class Qread:
    qr = []

    def decode_img(self, files, user):
        global COUNTER
        try:
            decoded_obj = decode(Image.open(files))
            l = len(decoded_obj)
            if l > 0:
                for obj in decoded_obj:
                    self.qr = obj.data.decode('utf-8')
                return self.qr
            else:
                return "Штрихкод не прочитался. " \
                       "Загрузи новое фото"
        except:
            print(files)
            return "Ошибка в чтении штрихкода"




# decode_obj.data.decode('utf-8')
