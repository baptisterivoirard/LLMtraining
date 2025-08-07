# importation des librairy
import imaplib
import email
from email.header import decode_header
import sys 
import time
import os
from dotenv import load_dotenv


# Fonction pour récuppérer les informations d'un mail et les mettre dans un dictionnaire (Sujet, envoyeur, corps, pièces jointes)
#contient plusieurs fonctions pour décoder chaque partie du mail et les rendre lisible
def affiche_info_email(email_message):
    mail_info = {}
    subject, encoding = decode_header(email_message["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")
    mail_info["Sujet :"]= subject

    sender, encoding = decode_header(email_message["From"])[0]
    if isinstance(sender, bytes):
        sender = sender.decode(encoding or "utf-8")
    mail_info["Envoyeur :"]= sender

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

    mail_info["Corps :"]= body
    mail_info["pièces jointes : "] = attachements
    return mail_info

# Fonction pour se connecter à la boite mail et récupérer les mails non lus. Chaque raw mail est décoder puis envoyer à la focntion affiche_infor_email() qui le traite
def email_recup():
    load_dotenv()
    # --- Config --- à mmettre dans un .env

    IMAP_SERVER = os.getenv("IMAP_SERVER")
    EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")
    EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")


    # --- Connexion IMAP ---
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

    # --- Sélection de la boîte de réception ---
    mail.select("inbox")

    # --- Récupération des mails non lus (ou tous si tu veux) ---
    status, messages = mail.search(None, "UNSEEN")  # ou "UNSEEN" pour non lus


    mail_ids = messages[0].split()  # Ex: [b'1', b'2', b'3']
    list_mails =[]
    for id in mail_ids:
        status, msg_data = mail.fetch(id, "(RFC822)")
        raw_email=msg_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        list_mails.append(affiche_info_email(email_message))
        print("nombre de mails en attente de traitement : ", len(list_mails))
    return list_mails


# Juste pour tester la fontion de récupération
if __name__ == "__main__":
    print (email_recup())
        











