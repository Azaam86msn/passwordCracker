# PasswordCracker

## Overview
PasswordCracker is a Python project that demonstrates the importance of secure password storage by attempting to crack passwords hashed with the SHA-1 algorithm. The program compares SHA-1 hashes against a dictionary of the top 10,000 most common passwords. It also supports salted hash cracking using known salts.

## Features
- Cracks passwords hashed using SHA-1.
- Optional support for salted hashes (both prepended and appended salts).
- Utilizes a dictionary attack for efficiency.
- Includes unit tests to validate functionality.

## Files
- **`password_cracker.py`**: Core implementation of the password-cracking function.
- **`main.py`**: Development entry point with example tests and hash cracking demonstrations.
- **`test_module.py`**: Unit tests to ensure the correctness of the password-cracking implementation.
- **`top-10000-passwords.txt`**: List of the 10,000 most common passwords.
- **`known-salts.txt`**: List of salts used for testing salted password hashes.

## How It Works
1. The program reads the `top-10000-passwords.txt` file to load common passwords.
2. If the `use_salts` flag is set to `True`, it loads salts from `known-salts.txt` and hashes each password with each salt (prepended and appended).
3. It compares the generated hashes with the input SHA-1 hash.
4. If a match is found, the plaintext password is returned; otherwise, it returns `"PASSWORD NOT IN DATABASE"`.

## Usage

### Running the Cracker
To use the password cracker, modify and run `main.py`:
```python
import password_cracker

# Crack unsalted hash
print(password_cracker.crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"))

# Crack salted hash
print(password_cracker.crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True))
```

### Running Tests
Run the unit tests with:
```bash
python -m unittest test_module.py
```

## Example
### Unsalted Hash Cracking
Input:  
`b305921a3723cd5d70a375cd21a61e60aabb84ec`  
Output:  
`sammy123`

### Salted Hash Cracking
Input:  
`53d8b3dc9d39f0184144674e310185e41a87ffd5` (with salts enabled)  
Output:  
`superman`

## Requirements
- Python 3.6 or higher
- `hashlib` (standard library)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Azaam86msn/passwordCracker.git
   cd passwordCracker
   ```
2. Ensure that `top-10000-passwords.txt` and `known-salts.txt` are in the root directory.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or new features.
