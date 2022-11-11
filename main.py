import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from work.running import run_qr

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/download/")
async def set_files(id_user: int, files: List[UploadFile] = File(...)):
    os.chdir("work/application")
    if os.path.exists(str(id_user) + "_img"):
        os.chdir(str(id_user) + "_img")
        for img in files:
            with open(f"{img.filename}", "wb") as buffer:
                shutil.copyfileobj(img.file, buffer)
                os.chdir("../")
                return {'QR': run_qr(id_user)}
    else:
        try:
            os.mkdir(str(id_user) + "_img")
            os.chdir(str(id_user) + "_img")
            for img in files:
                with open(f"{img.filename}", "wb") as buffer:
                    shutil.copyfileobj(img.file, buffer)
                    os.chdir("../")
                    return {'QR': run_qr(id_user)}
        except:
            print(os.getcwd())


@app.get("/api/getdata/")
async def get_files():
    return {'hello': "hello"}
