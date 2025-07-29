import imaplib
import email
from email.header import decode_header
import sys 
import time
import os
from dotenv import load_dotenv
from emailrecup import connect_to_email, affiche_info_email

def main ():
    while True:
        mail_ids, mail = connect_to_email()
        if not mail_ids:
            print("Pas de nouveaux mails.")
            time.sleep(60)
        list_mails =[]
        for id in mail_ids:
            msg_data = mail.fetch(id, "(RFC822)")
            raw_email=msg_data[0][1]
            if isinstance(raw_email, bytes):
                email_message = email.message_from_bytes(raw_email)
            else:
                email_message = email.message_from_string(raw_email)
            list_mails.append(affiche_info_email(email_message))
            print("nombre de mails en attente de traitement : ", len(list_mails))
            print(list_mails)
        

        time.sleep(60)



if __name__ == "__main__":
    main()
