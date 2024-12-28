from pystyle import *
import random
import string
import os
import requests

def generate_pseudo():
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    digits = ''.join(random.choices(string.digits, k=2))
    return letters + digits

def is_valid_pseudo(pseudo):
    if len(pseudo) == 4 and pseudo[:2].isalpha() and pseudo[2:].isdigit():
        return True
    return False

def check_discord_username(pseudo):
    url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": pseudo
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200 and response.json().get("username_attempt") == pseudo

def main():
    Write.Print(f"""
 __      ___               _____  ____     _____ ______ _   _
 \ \    / (_)             |  __ \|  _ \   / ____|  ____| \ | |
  \ \  / / _  _____      _| |  | | |_) | | |  __| |__  |  \| |
   \ \/ / | |/ _ \ \ /\ / | |  | |  _ <  | | |_ |  __| | . ` |
    \  /  | |  __/\ V  V /| |__| | |_) | | |__| | |____| |\  |
     \/   |_|\___| \_/\_/ |_____/|____/   \_____|______|_| \_|
                        .gg/viewdb                              """, Colors.blue_to_purple, interval=0)

    while True:
        print("Options:")
        print("1. Générer des pseudos")
        print("2. Vérifier les pseudos")
        print("3. Quitter")
        choice = input("Choisissez une option (1/2/3): ")

        if choice == '1':
            try:
                num_pseudos = int(input("Combien de pseudos voulez-vous générer ? "))
                if num_pseudos <= 0:
                    print("Veuillez entrer un nombre positif.")
                    continue

                filename = "pseudos.txt"
                with open(filename, "w") as file:
                    for _ in range(num_pseudos):
                        pseudo = generate_pseudo()
                        print(f"Pseudo généré: {Col.green}{pseudo}{Col.reset}")
                        file.write(pseudo + "\n")
                print(f"{num_pseudos} pseudos ont été générés et enregistrés dans '{filename}'.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        elif choice == '2':
            filename = "pseudos.txt"
            if not os.path.exists(filename):
                print(f"Le fichier '{filename}' n'existe pas. Veuillez générer des pseudos d'abord.")
                continue

            valid_filename = "valide.txt"
            with open(filename, "r") as file, open(valid_filename, "w") as valid_file:
                pseudos = file.readlines()

                print("\nVérification des pseudos :")
                for pseudo in pseudos:
                    pseudo = pseudo.strip()
                    if is_valid_pseudo(pseudo) and check_discord_username(pseudo):
                        print(f"{Col.green}{pseudo}{Col.reset} - Valide")
                        valid_file.write(pseudo + "\n")
                    else:
                        print(f"{Col.red}{pseudo}{Col.reset} - Invalide")

            print(f"Les pseudos valides ont été enregistrés dans '{valid_filename}'.")

        elif choice == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()
