# Template to be added in config folder with .env file
import os
from os.path import join, dirname
from dotenv import load_dotenv
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key(key_path):
    if os.path.exists(key_path):
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    else:
        raise FileNotFoundError(f"Key file '{key_path}' not found.")

def encrypt_value(value, key):
    cipher_suite = Fernet(key)
    encrypted_value = cipher_suite.encrypt(value.encode())
    return encrypted_value

def decrypt_value(encrypted_value, key):
    cipher_suite = Fernet(key)
    decrypted_value = cipher_suite.decrypt(encrypted_value).decode()
    return decrypted_value

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Path to the key file
key_path = 'C:\Scripts\Administration Scripts\Data Analysis Scripts\config\db_key.key'

# Load or generate the encryption key
if os.path.exists(key_path):
    key = load_key(key_path)
else:
    key = generate_key()
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

# Encrypt and save specific environment variables to .env file
encrypted_db_host = encrypt_value(os.environ.get("DB_HOST", ""), key)
encrypted_db_name = encrypt_value(os.environ.get("DB_NAME", ""), key)
encrypted_db_port = encrypt_value(os.environ.get("DB_PORT", ""), key)
encrypted_db_user = encrypt_value(os.environ.get("DB_USER", ""), key)
encrypted_db_pw = encrypt_value(os.environ.get("DB_PW", ""), key)


with open('C:\Scripts\Administration Scripts\Data Analysis Scripts\config\.env', 'w') as env_file:
    env_file.write(f'\nENCRYPTED_DB_HOST={encrypted_db_host.decode()}')
    env_file.write(f'\nENCRYPTED_DB_NAME={encrypted_db_name.decode()}')
    env_file.write(f'\nENCRYPTED_DB_PORT={encrypted_db_port.decode()}')
    env_file.write(f'\nENCRYPTED_DB_USER={encrypted_db_user.decode()}')
    env_file.write(f'\nENCRYPTED_DB_PW={encrypted_db_pw.decode()}')  

# Decrypt and use the environment variables
encrypted_db_host = os.getenv('ENCRYPTED_DB_HOST')
encrypted_db_name = os.getenv('ENCRYPTED_DB_NAME')
encrypted_db_port = os.getenv('ENCRYPTED_DB_PORT')
encrypted_db_user = os.getenv('ENCRYPTED_DB_USER')
encrypted_db_pw = os.getenv('ENCRYPTED_DB_PW')

if encrypted_db_host 
    and encrypted_db_name 
    and encrypted_db_port
    and encrypted_db_pw
    and encrypted_db_user:
        DB_HOST = decrypt_value(encrypted_db_host.encode(), key)
        DB_NAME = decrypt_value(encrypted_db_name.encode(), key)
        DB_PORT = decrypt_value(encrypted_db_port.encode(), key)
        DB_USER = decrypt_value(encrypted_db_user.encode(), key)
        DB_PW = decrypt_value(encrypted_db_pw.encode(), key)
        print("Decrypted DB_HOST")
        print("Decrypted DB_NAME")
        print("Decrypted DB_PORT")
        print("Decrypted DB_PW")
