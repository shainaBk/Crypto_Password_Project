"""
CLI.py
"""
import csv
import os
import Secure
import time


# Nom du fichier CSV qui agira comme base de données
DATABASE_FILENAME = 'users.csv'

# Vérifie si la base de données (fichier CSV) existe, sinon la crée
def init_db():
    if not os.path.exists(DATABASE_FILENAME):
        with open(DATABASE_FILENAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Username', 'Password']) # En-têtes du CSV

# Fonction pour s'inscrire
def signup():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    # Ici, ajoutez la logique pour le hachage et la sécurité du mot de passe
    if not Secure.check_password_strength(password):
        print("Password is too weak. It must be at least 13 characters long with a mix of letters and numbers.")
        clear2s() 
        return
    hashed_password = Secure.get_hash_password(password).decode('utf-8')

    # Écriture dans le fichier CSV
    with open(DATABASE_FILENAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, hashed_password])
    print("Registration successful!")
    clear2s()

# Fonction pour se connecter
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in attempt_tracker and attempt_tracker[username] >= 3:
        if time.time() - last_attempt_time[username] < 300:  # Bloquer pendant 5 minutes
            print("Too many failed attempts. Please try again later.")
            clear2s()
            return
        else:
            attempt_tracker[username] = 0  # Réinitialise le compteur après le délai

    with open(DATABASE_FILENAME, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        found = False  # Indicateur si l'utilisateur est trouvé
        for row in reader:
            user_hashed_password = row['Password']
            user_hashed_password_bytes = user_hashed_password.encode('utf-8')
            if row['Username'] == username and Secure.check_user_password(password, user_hashed_password_bytes):
                found = True  # L'utilisateur est trouvé et le mot de passe correspond
                break

        if not found:
            print("Invalid username or password!")
            attempt_tracker[username] = attempt_tracker.get(username, 0) + 1
            last_attempt_time[username] = time.time()
            clear2s()
        else:
            # Réinitialisez le compteur d'essais après une connexion réussie
            if username in attempt_tracker:
                del attempt_tracker[username]
            if username in last_attempt_time:
                del last_attempt_time[username]
            print("Login successful!")
            clear2s()



def clear2s():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear') 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu principal du CLI
def main_menu():
    while True:
        print(attempt_tracker)
        print("\n--- Main Menu ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            clear()
            signup()
        elif choice == '2':
            clear()
            login()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            clear()

if __name__ == "__main__":
    init_db()
    attempt_tracker = {}  # Suit le nombre de tentatives échouées
    last_attempt_time = {}  # Suit le temps de la dernière tentativ
    main_menu()
