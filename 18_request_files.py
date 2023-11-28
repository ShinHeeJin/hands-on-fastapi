from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# Define File Parameters
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


# File Parameters with UploadFile
@app.post("/uploadfild/")
async def create_upload_file(file: UploadFile):
    """
    # Using UploadFile has several advantages over bytes:

    1. You don't have to use File() in the default value of the parameter.
    2. It uses a "spooled" file:
        * A file stored in memory up to a maximum size limit, and after passing this limit it will be stored in disk.
    3. This means that it will work well for large files like images, videos, large binaries, etc. without consuming all the memory.

    # UploadFile has the following async methods.
    As all these methods are async methods, you need to "await" them.
    content = await file.read()
    """
    print(f"{type(file)=}")  # =<class 'starlette.datastructures.UploadFile'>
    return {"filename": file.filename}
