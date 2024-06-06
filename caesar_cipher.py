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
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def get_valid_choice():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (e/d) or 'q' to quit: ").lower()
        if choice in ['e', 'd', 'q']:
            return choice
        print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

def main():
    print("Welcome to the Caesar Cipher Program")
    while True:
        choice = get_valid_choice()
        if choice == 'q':
            print("Goodbye!")
            break
        message = input("Enter your message: ")
        shift = get_valid_shift()
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
