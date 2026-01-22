import os, smtplib, ssl
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL")
PWD = os.getenv("EMAIL_PWD")

print("EMAIL:", EMAIL)
print("PWD length:", len(PWD) if PWD else None)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as s:
    s.login(EMAIL, PWD)
    print("✅ Logged in successfully")
