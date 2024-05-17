import sys
from ui_UI import Ui_MainWindow as ui
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import secrets

print(secrets.token_bytes(32))

SECRET_KEY = b"my_secret_key_123"  # 16 bytes for AES-128


def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return kdf.derive(password)


def encrypt_message(message: str, key: bytes) -> str:
    salt = os.urandom(16)
    derived_key = derive_key(key, salt)
    iv = os.urandom(16)
    cipher = Cipher(
        algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
    )
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return urlsafe_b64encode(salt + iv + encrypted_message).decode()


def decrypt_message(encrypted_message: str, key: bytes) -> str:
    encrypted_message = urlsafe_b64decode(encrypted_message)
    salt = encrypted_message[:16]
    iv = encrypted_message[16:32]
    encrypted_data = encrypted_message[32:]
    derived_key = derive_key(key, salt)
    cipher = Cipher(
        algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_message.decode()


print(
    decrypt_message(
        "6T8fqI0JJD4VU96A3PPS-80Y_f754pqxJ1_1rqErxngSNZnYpaLP0QujqGUOMz5vz40Teybf2w8a1X1jtcvUwgoI8pc=",
        SECRET_KEY,
    )
)
