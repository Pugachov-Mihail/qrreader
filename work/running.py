from work.qread import Qread
from work.indexer import Indexer

index = Indexer()
qr = Qread()


def run_qr(user):
    for img in index.url_img_of_folder():
        mes = qr.decode_img(img, user)
        message = index.get_url_folder_user(user, mes)
        return message

