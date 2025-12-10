import hashlib, os

pepper = b"SUPER_SECRET_PEPPER"

def hash_plain(pw):
    return hashlib.sha256(pw).hexdigest()

def hash_with_salt(pw):
    salt = os.urandom(16)
    return salt, hashlib.sha256(salt + pw).hexdigest()

def hash_salt_pepper(pw):
    salt = os.urandom(16)
    return salt, hashlib.sha256(salt + pw + pepper).hexdigest()

pw = b"q@q"

print("NO SALT (same hash twice):")
print(hash_plain(pw))
print(hash_plain(pw))

print("\nWITH SALT (different each time):")
print(hash_with_salt(pw))
print(hash_with_salt(pw))

print("\nWITH SALT + PEPPER:")
print(hash_salt_pepper(pw))