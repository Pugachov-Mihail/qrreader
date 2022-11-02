import os
from fastapi import FastAPI, UploadFile, File
from typing import List
import shutil

app = FastAPI()


@app.post("/api/download/")
async def set_files(id_user: int, files: List[UploadFile] = File(...)):
        os.chdir("application")
        if os.path.exists(str(id_user)+"_img"):
            os.chdir(str(id_user)+"_img")
            for img in files:
                with open(f"{img.filename}", "wb") as buffer:
                    shutil.copyfileobj(img.file, buffer)
                    os.chdir("../../")
                    return {'file_name': "ok"}
        else:
            os.mkdir(str(id_user)+"_img")
            os.chdir(str(id_user)+"_img")
            for img in files:
                with open(f"{img.filename}", "wb") as buffer:
                    shutil.copyfileobj(img.file, buffer)
                    os.chdir("../../")
                    return {'file_name': "ok"}


@app.get("/api/getdata/")
async def get_files():
    return {'hello' : "hello"}