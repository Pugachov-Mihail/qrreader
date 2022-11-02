import os

#os.chdir("../")
        #os.chdir(self.path)
        #print(os.getcwd())

class Indexer:
    files = []
    folders = []

    def __init__(self, path):
        self.path = path
        os.chdir("../")
        print(os.getcwd())

    def index_folder(self, path):
        try:
            folders = os.listdir(path)
            self.folders.append(folders)
            for folder in self.folders:
                return folder
        except:
            print("Error folder")

    def index_filex_of_folder(self):
        try:
            for folder in self.index_folder("application"):
                files_in_folder = os.listdir(folder)
                print(files_in_folder)
        except:
            print(self.files)


a = Indexer("application")
a.index_filex_of_folder()
