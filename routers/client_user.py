from fastapi import APIRouter, HTTPException, Depends
from database import db
from auth import get_password_hash, create_access_token, verify_password
from models import User, DownloadLinkResponse
from utils import encrypt_id, decrypt_token

router = APIRouter(prefix="/client", tags=["Client User"])

@router.post("/signup")
async def signup(user: User):
    hashed = get_password_hash(user.password)
    result = await db.users.insert_one({"email": user.email, "password": hashed, "role": "client", "is_verified": False})
    token = encrypt_id(str(result.inserted_id))
    return {"verification_url": f"/client/verify/{token}"}

@router.get("/verify/{token}")
async def verify_email(token: str):
    user_id = decrypt_token(token)
    await db.users.update_one({"_id": user_id}, {"$set": {"is_verified": True}})
    return {"message": "Email verified"}

@router.post("/login")
async def login(user: User):
    db_user = await db.users.find_one({"email": user.email, "role": "client"})
    if not db_user or not verify_password(user.password, db_user['password']):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user["_id"])})
    return {"access_token": token}

@router.get("/files")
async def list_files():
    files = await db.files.find().to_list(100)
    return files

@router.get("/download-file/{file_id}", response_model=DownloadLinkResponse)
async def get_download_link(file_id: str):
    token = encrypt_id(file_id)
    return {"download_link": f"/client/download/{token}", "message": "success"}

@router.get("/download/{token}")
async def download_file(token: str):
    file_id = decrypt_token(token)
    file = await db.files.find_one({"_id": file_id})
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return {"filename": file['filename'], "message": "Download initiated"}