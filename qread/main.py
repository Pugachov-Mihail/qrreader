from .qread import Qread
from .indexer import Indexer

index = Indexer()
qr = Qread()


def run_qr(user):
    for img in index.url_img_of_folder():
        message = index.get_url_folder_user(user, qr.decode_img(img, user))
        return message
