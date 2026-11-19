# File Protection Utility

A Python-based cybersecurity project for protecting sensitive files using AES-256-GCM encryption and password-based key derivation.

**Project Domain:** Cyber Security  
**Programming Language:** Python 3.12  
**Author:** Mihir Koshti

---

## Project Overview

File Protection Utility is a command-line application developed to encrypt and decrypt sensitive files using a password.

It uses AES-256-GCM encryption to protect file contents and PBKDF2-HMAC-SHA256 to generate a secure encryption key from the user's password.

The application also verifies file integrity during decryption. If the password is incorrect or the encrypted file has been modified, the decryption process is rejected.

## Objectives

- Protect sensitive files from unauthorized access.
- Implement AES-256-GCM encryption.
- Generate secure keys using PBKDF2.
- Encrypt normal files into encrypted format.
- Decrypt files using the correct password.
- Detect incorrect passwords and modified encrypted files.

## Features

- File Encryption
- File Decryption
- AES-256-GCM Encryption
- PBKDF2 Password-Based Key Derivation
- SHA-256 Hash Algorithm
- Random Salt Generation
- Secure Nonce Generation
- File Integrity Verification
- Wrong Password Detection
- Command-Line Interface

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming Language |
| AES-256-GCM | Encryption and Decryption |
| PBKDF2 | Key Generation |
| SHA-256 | Hash Algorithm |
| Cryptography Library | Cryptographic Operations |
| Visual Studio Code | Development Environment |

## Security Configuration

| Parameter | Value |
|---|---|
| Encryption Algorithm | AES-256-GCM |
| Key Size | 256 bits |
| Salt Size | 16 bytes |
| Nonce Size | 12 bytes |
| Key Derivation | PBKDF2-HMAC-SHA256 |
| Iterations | 600,000 |

## Installation

**Step 1: Clone the Repository**

```bash
git clone https://github.com/0805-mihir/file-protection-utility.git
```

**Step 2: Open Project Folder**

```bash
cd file-protection-utility
```

**Step 3: Install Required Library**

```bash
pip install cryptography
```

## How to Run

```bash
python file_protection_utility.py
```

## How to Use

**File Encryption**

1. Select option 1.
2. Enter the input file name.
3. Enter the output encrypted file name.
4. Enter a password.
5. The program creates an encrypted `.enc` file.

**File Decryption**

1. Select option 2.
2. Enter the encrypted file name.
3. Enter the output file name.
4. Enter the correct password.
5. The program restores the original file after successful authentication.

## Testing

| Test Case | Result |
|---|---|
| Successful File Encryption | Passed |
| Successful File Decryption | Passed |
| Wrong Password Verification | Passed |
| Tampered File Verification | Passed |

## Project Structure

```text
file-protection-utility/
│
├── file_protection_utility.py
├── sample.txt
└── README.md
```

## Security Note

- Always use a strong password.
- Keep your password confidential.
- Maintain a backup of important original files.
- A lost password cannot be recovered through this application.

## Future Scope

- Graphical User Interface (GUI).
- Multiple File and Folder Encryption.
- Cloud Storage Integration.
- Password Strength Checker.
- Cross-Platform Support.

## Author

**Mihir Koshti**

Cybersecurity Project | Python Development

## References

- Python Documentation: https://docs.python.org/3/
- Cryptography Documentation: https://cryptography.io/en/latest/
- NIST AES Standard: https://csrc.nist.gov/pubs/fips/197/final
- NIST Password-Based Key Derivation: https://csrc.nist.gov/pubs/sp/800/132/final
