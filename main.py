import imaplib
import email
from email.header import decode_header
import sys 
import time
import os
from dotenv import load_dotenv
from emailrecup import email_recup
from llmresponse import reponse_llm
from emailanswerer import send_email

def main ():
    while True:
        list_mails=[]
        list_mails=email_recup()
        # print(list_mails)
        for mail in list_mails:
            print(mail)
            reponse= reponse_llm(mail)
            print(reponse)
            if "[" in reponse and "]" in reponse :
                print("Le LLM a besoin de plus d'informations pour completer la réponse.")
                while "[" in reponse and "]" in reponse:
                    start = reponse.index("[")
                    end = reponse.index("]", start)
                    placeholder = reponse[start:end+1]
                    user_input = input(f"{placeholder} : ")
                    reponse = reponse.replace(placeholder, user_input, 1)
            print(reponse)
            print("Mail prêt à l'envoi, envoyer ? (O/N)")
            send = input()
            if send.lower() == "o":
                load_dotenv()
                print("Envoi du mail...")
                send_email(mail["Envoyeur :"].split("<")[1].strip(">"), "Re:"+ mail["Sujet :"], reponse, os.getenv("EMAIL_ACCOUNT"), os.getenv("EMAIL_PASSWORD"))
                print("Mail envoyé !")

            


        time.sleep(30)
        print("Vérification des nouveaux mails...")



if __name__ == "__main__":
    main()
