from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

class FileUploadResponse(BaseModel):
    filename: str
    message: str

class DownloadLinkResponse(BaseModel):
    download_link: str
    message: str

