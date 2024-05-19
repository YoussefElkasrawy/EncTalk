import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import secrets

#print(secrets.token_bytes(32))

def get_password_from_user():
    # In a real application, you'd likely prompt the user for their password securely
    # For simplicity here, we'll just use an input statement
    return input("Enter your password: ").encode()

def derive_key(password: bytes, salt: bytes) -> bytes:
    print("Password:", password)
    print("Salt:", salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    derived_key = kdf.derive(password)
    print("Derived Key:", derived_key)
    return derived_key


def encrypt_message(message: str, password: bytes) -> str:
    salt = os.urandom(16)
    derived_key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(
        algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
    )
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return urlsafe_b64encode(salt + iv + encrypted_message).decode()


def decrypt_message(encrypted_message: str, password: bytes) -> str:
    encrypted_message = urlsafe_b64decode(encrypted_message)
    salt = encrypted_message[:16]
    iv = encrypted_message[16:32]
    encrypted_data = encrypted_message[32:]
    print("Salt:", salt)
    print("IV:", iv)
    print("Encrypted Data:", encrypted_data)
    derived_key = derive_key(password, salt)
    print("Derived Key:", derived_key)
    cipher = Cipher(
        algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_data) + decryptor.finalize()
    print("Decrypted Message:", decrypted_message)
    return decrypted_message.decode()


password = get_password_from_user()
print(
    decrypt_message(
        "6T8fqI0JJD4VU96A3PPS-80Y_f754pqxJ1_1rqErxngSNZnYpaLP0QujqGUOMz5vz40Teybf2w8a1X1jtcvUwgoI8pc=",
        password
    )
)
