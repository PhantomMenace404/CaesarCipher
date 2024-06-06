import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def get_valid_shift():
    while True:
        try:
            shift = int(input(Fore.YELLOW + "Enter shift value: " + Style.RESET_ALL))
            return shift
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer value.")

def get_valid_choice():
    while True:
        choice = input(Fore.CYAN + "Would you like to encrypt or decrypt a message? (e/d) or 'q' to quit: " + Style.RESET_ALL).lower()
        if choice in ['e', 'd', 'q']:
            return choice
        print(Fore.RED + "Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

def get_continue_choice():
    while True:
        choice = input(Fore.CYAN + "Would you like to perform another action? (y/n): " + Style.RESET_ALL).lower()
        if choice in ['y', 'n']:
            return choice
        print(Fore.RED + "Invalid choice. Please enter 'y' to continue or 'n' to quit.")

def main():
    print(Fore.GREEN + Style.BRIGHT + """
  ____     _     _____  ____      _     ____     ____  ___  ____   _   _  _____  ____  
 / ___|   / \   | ____|/ ___|    / \   |  _ \   / ___||_ _||  _ \ | | | || ____||  _ \
| |      / _ \  |  _|  \___ \   / _ \  | |_) | | |     | | | |_) || |_| ||  _|  | |_) |
| |___  / ___ \ | |___  ___) | / ___ \ |  _ <  | |___  | | |  __/ |  _  || |___ |  _ <
 \____|/_/   \_\|_____||____/ /_/   \_\|_| \_\  \____||___||_|    |_| |_||_____||_| \_\

    """ + Style.RESET_ALL)
    print(Fore.GREEN + "Welcome to the Caesar Cipher Program" + Style.RESET_ALL)
    while True:
        choice = get_valid_choice()
        if choice == 'q':
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break
        message = input(Fore.YELLOW + "Enter your message: " + Style.RESET_ALL)
        shift = get_valid_shift()
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(Fore.GREEN + f"Encrypted message: {encrypted_message}" + Style.RESET_ALL)
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print(Fore.GREEN + f"Decrypted message: {decrypted_message}" + Style.RESET_ALL)

        continue_choice = get_continue_choice()
        if continue_choice == 'n':
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
