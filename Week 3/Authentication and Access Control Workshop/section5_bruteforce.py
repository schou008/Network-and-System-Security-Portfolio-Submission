import hashlib

common = ["password","123456","letmein","qwerty"]

target = hashlib.md5("password".encode()).hexdigest()

print("Target hash:", target)

for pw in common:
    if hashlib.md5(pw.encode()).hexdigest() == target:
        print("Cracked:", pw)
        break
