import os
from qread.config import URL_FOLDERS


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

    def get_url_folder_user(self, user, callback):
        try:
            if f'{user}_img' in self.img \
                    or os.path.exists(str(user) + "_img"):
                os.rmdir(f'{user}_img')
            else:
                try:
                    return callback
                except:
                    print('Tyt')
        except:
            print(os.getcwd())
            print("Ошибочка вышла")


    def information_on_delete(self):
        print(self.url_img_of_folder())
