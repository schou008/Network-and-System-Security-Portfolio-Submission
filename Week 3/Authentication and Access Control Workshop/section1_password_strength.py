import math
import string

def password_entropy(pw):
    pool = 0
    if any(c.islower() for c in pw): pool += 26
    if any(c.isupper() for c in pw): pool += 26
    if any(c.isdigit() for c in pw): pool += 10
    if any(c in string.punctuation for c in pw): pool += len(string.punctuation)
    return len(pw) * math.log2(pool) if pool else 0

def password_strength(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if len(pw) >= 12: score += 1
    score += any(c.islower() for c in pw)
    score += any(c.isupper() for c in pw)
    score += any(c.isdigit() for c in pw)
    score += any(c in string.punctuation for c in pw)
    bad = ['password','123456','qwerty','letmein']
    if pw.lower() in bad:
        score = 0
    return score, password_entropy(pw)

if __name__ == '__main__':
    pw = input("Enter password: ")
    s,e = password_strength(pw)
    print("Score:", s, "Entropy:", e)
