import pyotp, qrcode

totp = pyotp.TOTP(pyotp.random_base32())
print("Secret:", totp.secret)

uri = totp.provisioning_uri(name="q", issuer_name="w")
img = qrcode.make(uri)
img.save("totp_qr.png")

print("Scan totp_qr.png with Google Authenticator.")
print("Current code:", totp.now())
