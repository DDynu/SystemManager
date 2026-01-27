from base64 import b64encode
import secrets
import hashlib

def id_gen(username):
    username_token = b64encode(username.encode())
    return b64encode(username_token).decode()

def password_gen(password: str):
    salt = secrets.token_bytes(16)
    print("SALT", salt)
    hashed_password = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    return salt + hashed_password

def password_check(password: str, stored_password: bytes) -> bool:
    salt = stored_password[:16]
    hashed_password = stored_password[16:]
    # Compute the key
    key = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    # Verify key
    return key == hashed_password
