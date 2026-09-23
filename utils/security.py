import hashlib

def chiffrer_motdepasse(password):
    return hashlib.sha256(
        password.encode()
        ).hexdigest()

if __name__ == "__main__":
    print(chiffrer_motdepasse("bonjour123"))
    