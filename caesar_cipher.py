def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    print("Welcome to the Caesar Cipher Program")
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (e/d) or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        elif choice.lower() in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter shift value: "))
            if choice.lower() == 'e':
                print(f"Encrypted message: {encrypt(message, shift)}")
            elif choice.lower() == 'd':
                print(f"Decrypted message: {decrypt(message, shift)}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
