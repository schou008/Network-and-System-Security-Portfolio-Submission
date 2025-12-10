import hashlib, bcrypt

pw = b"q@q"

print("MD5:", hashlib.md5(pw).hexdigest())
print("SHA-256:", hashlib.sha256(pw).hexdigest())

hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
print("bcrypt:", hashed)

print("Verify:", bcrypt.checkpw(pw, hashed))
