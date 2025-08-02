import imaplib
import email
from email.header import decode_header
import sys 
import time
import os
from dotenv import load_dotenv
from emailrecup import email_recup
from llmresponse import reponse_llm

def main ():
    while True:
        list_mails=[]
        list_mails=email_recup()
        # print(list_mails)
        for mail in list_mails:
            print(mail)
            reponse= reponse_llm(mail)
            print(reponse)


        time.sleep(30)
        print("Vérification des nouveaux mails...")



if __name__ == "__main__":
    main()
