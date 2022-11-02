import os

URL_FOLDERS = {
    "application": "application",
}
COUNTER = True


class Indexer:
    files = []
    folders = []

    def __init__(self, path):
        self.path = path
        os.chdir("../")

    def index_folder(self):
        folders = os.listdir(URL_FOLDERS["application"])
        self.folders.append(folders)
        for folder in self.folders:
            print(self.folders)
            return folder


a = Indexer("application")
a.index_folder()

dir_count = len(next(os.walk(URL_FOLDERS["application"]))[1])
#while len(self.folders) == dir_count: