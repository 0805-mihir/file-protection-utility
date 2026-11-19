
import os
import argparse
import getpass

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# Security Configuration
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
ITERATIONS = 600000


# Generate Encryption Key using PBKDF2
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS
    )

    return kdf.derive(password.encode("utf-8"))


# Encrypt File
def encrypt_file(input_file, output_file, password):
    try:
        with open(input_file, "rb") as file:
            file_data = file.read()

        salt = os.urandom(SALT_SIZE)
        nonce = os.urandom(NONCE_SIZE)

        key = derive_key(password, salt)

        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, file_data, None)

        with open(output_file, "wb") as file:
            file.write(salt + nonce + ciphertext)

        print("\n[+] File encrypted successfully!")
        print(f"[+] Encrypted file: {output_file}")

    except OSError as error:
        print(f"\n[!] File error: {error}")


# Decrypt File
def decrypt_file(input_file, output_file, password):
    try:
        with open(input_file, "rb") as file:
            encrypted_data = file.read()

        minimum_size = SALT_SIZE + NONCE_SIZE + 16

        if len(encrypted_data) < minimum_size:
            print("\n[!] Invalid or corrupted encrypted file.")
            return

        salt = encrypted_data[:SALT_SIZE]
        nonce = encrypted_data[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
        ciphertext = encrypted_data[SALT_SIZE + NONCE_SIZE:]

        key = derive_key(password, salt)

        aesgcm = AESGCM(key)

        try:
            decrypted_data = aesgcm.decrypt(
                nonce,
                ciphertext,
                None
            )
        except Exception:
            print("\n[!] Decryption failed!")
            print("[!] Wrong password or file integrity check failed.")
            return

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("\n[+] File decrypted successfully!")
        print(f"[+] Restored file: {output_file}")
        print("[+] Authentication successful. File integrity verified.")

    except OSError as error:
        print(f"\n[!] File error: {error}")


# Main Program
def main():
    parser = argparse.ArgumentParser(
        description="AES-256 File Protection Utility"
    )

    parser.add_argument(
        "operation",
        choices=["encrypt", "decrypt"],
        help="Choose encrypt or decrypt"
    )

    parser.add_argument(
        "input_file",
        help="Path of input file"
    )

    parser.add_argument(
        "output_file",
        help="Path of output file"
    )

    args = parser.parse_args()

    password = input("Enter password: ")

    if not password:
        print("[!] Password cannot be empty.")
        return

    if args.operation == "encrypt":
        encrypt_file(
            args.input_file,
            args.output_file,
            password
        )

    elif args.operation == "decrypt":
        decrypt_file(
            args.input_file,
            args.output_file,
            password
        )


if __name__ == "__main__":
    main()
