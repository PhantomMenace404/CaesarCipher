# Caesar Cipher

This is a simple Python program that encrypts and decrypts text using the Caesar Cipher algorithm. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt messages by shifting letters.
- Decrypt messages by reversing the shift.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetic characters during encryption/decryption.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Prerequisites

- Python 3.x: This program requires Python version 3.x. You can check your Python version by running `python --version` or `python3 --version` in your terminal. If you do not have Python 3.x installed, you can download it from the [official Python website](https://www.python.org/downloads/).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/PhantomMenace404/PRODIGY_CS_01.git
    cd PRODIGY_CS_01
    ```

2. **Run the script**:
    ```bash
    python caesar_cipher.py
    ```

## Usage

1. When you run the script, you'll be greeted with a welcome message.
2. Follow the on-screen prompts to choose whether to encrypt or decrypt a message.
3. Enter the message you wish to process.
4. Enter the shift value (an integer) to use for encryption or decryption.
5. The program will output the encrypted or decrypted message.

### Example

```plaintext
  ____     _     _____  ____      _     ____     ____  ___  ____   _   _  _____  ____  
 / ___|   / \   | ____|/ ___|    / \   |  _ \   / ___||_ _||  _ \ | | | || ____||  _ \
| |      / _ \  |  _|  \___ \   / _ \  | |_) | | |     | | | |_) || |_| ||  _|  | |_) |
| |___  / ___ \ | |___  ___) | / ___ \ |  _ <  | |___  | | |  __/ |  _  || |___ |  _ <
 \____|/_/   \_\|_____||____/ /_/   \_\|_| \_\  \____||___||_|    |_| |_||_____||_| \_\

Welcome to the Caesar Cipher Program

Would you like to encrypt or decrypt a message? (e/d) or 'q' to quit: e
Enter your message: Hello
Enter shift value: 3
Encrypted message: Khoor

Would you like to perform another action? (y/n): y

Would you like to encrypt or decrypt a message? (e/d) or 'q' to quit: d
Enter your message: Khoor
Enter shift value: 3
Decrypted message: Hello

Would you like to perform another action? (y/n): n

Goodbye!

