from fastapi import APIRouter, Depends, UploadFile, HTTPException
from file_handler import save_file
from database import db
from auth import verify_password, create_access_token, get_current_user
from models import User

router = APIRouter(prefix="/ops", tags=["Ops User"])

@router.post("/login")
async def login(user: User):
    db_user = await db.users.find_one({"email": user.email, "role": "ops"})
    if not db_user or not verify_password(user.password, db_user['password']):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user["_id"])})
    return {"access_token": token}

@router.post("/upload")
async def upload(file: UploadFile, current_user: User = Depends(get_current_user)):
    filename = await save_file(file)
    result = await db.files.insert_one({"filename": filename})
    return {"message": "file uploaded", "filename": filename}
