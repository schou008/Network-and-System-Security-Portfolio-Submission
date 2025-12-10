import bcrypt, pyotp
from section1_password_strength import password_strength

class AuthSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, pw):
        score, _ = password_strength(pw)
        if score < 4:
            return "Weak password rejected."

        hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        totp = pyotp.random_base32()

        self.users[username] = {"hash": hashed, "totp": totp}
        return f"User {username} registered. TOTP secret: {totp}"

    def authenticate(self, username, pw, code):
        user = self.users.get(username)
        if not user:
            return "User not found."

        if not bcrypt.checkpw(pw.encode(), user["hash"]):
            return "Password incorrect."

        totp = pyotp.TOTP(user["totp"])
        if not totp.verify(code):
            return "Invalid TOTP code."

        return "Authentication successful!"

if __name__=='__main__':
    auth = AuthSystem()
    print(auth.register_user("q", "MyS3cur3!Pass"))
