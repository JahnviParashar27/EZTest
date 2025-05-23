from cryptography.fernet import Fernet

fernet = Fernet(Fernet.generate_key())

def encrypt_id(file_id: str) -> str:
    return fernet.encrypt(file_id.encode()).decode()

def decrypt_token(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()