import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as password_file:
        passwords = [line.strip() for line in password_file]
    
    # If salts are required, load the salt values
    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as salt_file:
            salts = [line.strip() for line in salt_file]
    
    # Function to hash a password
    def sha1_hash(password):
        return hashlib.sha1(password.encode()).hexdigest()
    
    # Check for salted or unsalted matches
    if use_salts:
        for salt in salts:
            for password in passwords:
                # Test both prepend and append combinations of salt
                if sha1_hash(salt + password) == hash or sha1_hash(password + salt) == hash:
                    return password
    else:
        for password in passwords:
            if sha1_hash(password) == hash:
                return password
    
    # If no match is found
    return "PASSWORD NOT IN DATABASE"
