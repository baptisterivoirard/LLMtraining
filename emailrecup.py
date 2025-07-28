import imaplib
import email
from email.header import decode_header
import sys 
import time

# --- Config --- à mmettre dans un .env
IMAP_SERVER = "mail.mailo.com"
EMAIL_ACCOUNT = "lmtraining@mailo.com"
EMAIL_PASSWORD = "nsYMhH6p*Yd.u6G"





def affiche_info_email(email_message):
    subject, encoding = decode_header(email_message["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")
    print("Sujet :", subject)

    sender, encoding = decode_header(email_message["From"])[0]
    if isinstance(sender, bytes):
        sender = sender.decode(encoding or "utf-8")
    print("Envoyeur :", sender)

    body = ""
    attachements={}
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass
            elif "attachment" in content_disposition:
                filename = part.get_filename()
                charset = part.get_content_charset()
                content = part.get_payload(decode=True)
                decoded_text = content.decode(charset or "utf-8", errors="replace")
                attachements[filename]= decoded_text
    else:
        body = email_message.get_payload(decode=True).decode()

    print("Corps :", body)
    print("pièces jointes : " , attachements)
    return subject, sender, body, attachements



while True:
    # --- Connexion IMAP ---
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

# --- Sélection de la boîte de réception ---
    mail.select("inbox")

# --- Récupération des mails non lus (ou tous si tu veux) ---
    status, messages = mail.search(None, "UNSEEN")  # ou "UNSEEN" pour non lus


    mail_ids = messages[0].split()  # Ex: [b'1', b'2', b'3']

    for id in mail_ids:
        status, msg_data = mail.fetch(id, "(RFC822)")
        raw_email=msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        affiche_info_email(email_message)
    time.sleep(60)









