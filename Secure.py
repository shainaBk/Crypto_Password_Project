import bcrypt
import math
from tink import aead, core, deaed

def check_password_strength(password):
    N = 36  # Nombre de symboles possibles pour un ensemble alphanumérique insensible à la casse
    L = len(password)  # Longueur du mot de passe
    entropy = L * math.log2(N)
    return entropy >= 64  # Vérifie si l'entropie est d'au moins 64 bits

def get_hash_password(password):
    # Convertit le mot de passe en bytes et génère un sel
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def check_user_password(password,userPassword):
    return  bcrypt.checkpw(password, userPassword)