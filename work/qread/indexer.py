import os
import shutil
from qread.config import URL_FOLDERS, COUNTER


class Indexer:
    """Собирает информацию по именам папок,
    фотографий и созданий урлов от их названия"""
    files = []
    folders = []
    img = []

    def index_folder(self):
        # Сохраняет названия папок пользователей которые загружали фотографии,
        # данный метод можно не вызывать он тянется в классе
        folders = os.listdir(URL_FOLDERS["application"])
        self.folders.append(folders)
        for folder in self.folders:
            return folder

    def create_url_img(self):
        # создание урла полного урл хранящий в себе application + id user
        for folder in self.index_folder():
            self.files.append(f'{URL_FOLDERS["application"]}/{folder}')
        return self.files

    def url_img_of_folder(self):
        # генерация урла который дальше идет в qr ридер
        imgs = []
        try:
            for urls in self.create_url_img():
                try:
                    imgs = os.listdir(urls)
                    for de in self.files:
                        if self.files.count(de) > 1:
                            self.files.remove(de)
                        else:
                            continue
                except:
                    print("Error find images: code 2")
            for url in imgs:
                self.img.append(urls + '/' + url)
        except:
            print("Error find images: code 1")
        return self.img

    def get_url_folder_user(self, user, qr_message):
        call_text = "Штрихкод не прочитался. " \
                       "Загрузи новое фото"

        call_text2 = "Ошибка в чтении штрихкода"

        os.chdir(URL_FOLDERS['application'])
        if qr_message == call_text and qr_message == call_text2:
            return qr_message
        if os.path.exists(str(user) + "_img"):
            shutil.rmtree(str(user) + "_img", ignore_errors=True)
            os.chdir("../")
        return qr_message
