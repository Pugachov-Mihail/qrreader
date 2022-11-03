from .qread import Qread
from .indexer import Indexer
import os


index = Indexer()
qr = Qread()

class QrIndex:
    a = index.index_folder()
    b = index.create_url_img()
    c = index.get_url_img_of_folder()
    d = index.delete_foldes()
    def printic(self):
        print(self.a)
        print(self.b)
        print(self.c)



def run_qr():
   for img in index.get_url_img_of_folder():
     print(img)
     message = qr.decode_img(img)
     return message





