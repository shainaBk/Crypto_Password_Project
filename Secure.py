"""
Secure.py
"""
import bcrypt
import math
import os
from dotenv import load_dotenv

# Chargez les variables d'environnement à partir du fichier '.env'
load_dotenv()

# Récupérez le pepper à partir des variables d'environnement
PEPPER = os.getenv('PEPPER')

def check_password_strength(password):
    N = 36  # Nombre de symboles possibles pour un ensemble alphanumérique insensible à la casse
    L = len(password)  # Longueur du mot de passe
    entropy = L * math.log2(N)
    return entropy >= 64  # Vérifie si l'entropie est d'au moins 64 bits

def get_hash_password(password):
    # Convertit le mot de passe en bytes et génère un sel
    password_peppered = password + PEPPER
    password_bytes = password_peppered.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def check_user_password(password,userPassword):
    password_peppered = password + PEPPER
    password_peppered_bytes = password_peppered.encode('utf-8')
    return  bcrypt.checkpw(password_peppered_bytes, userPassword)