import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

def send_email(to_email, subject, body, from_email, password):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(body)

    # Connexion au serveur SMTP de ton fournisseur
    with smtplib.SMTP_SSL("smtp.mailo.com", 465) as smtp:  # ou smtp.gmail.com
        smtp.login(from_email, password)
        smtp.send_message(msg)


if __name__ == "__main__":
    load_dotenv()
    EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")
    EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")
    TO_email ="rivoirardbaptiste2@gmail.com"
    SUBJECT = "test"
    BODY = "Ceci est un test d'envoi automatisé d'email."

    send_email(TO_email, SUBJECT, BODY, EMAIL_ACCOUNT, EMAIL_PASSWORD)
    print("Test")