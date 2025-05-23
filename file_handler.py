import os
from fastapi import UploadFile

ALLOWED_TYPES = ["application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                 "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                 "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

async def save_file(file: UploadFile):
    if file.content_type not in ALLOWED_TYPES:
        raise ValueError("Unsupported file type")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return file.filename