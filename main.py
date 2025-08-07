# importation des librairy
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


# Fonction principale qui gère tout de bout en bout
def main ():
    while True:
        list_mails=[]
        list_mails=email_recup() # Récupère les mails non lus et met dans une liste
        
        for mail in list_mails:
            print(mail)
            reponse= reponse_llm(mail) # Génère la réponse par le LLM pour chaque mail
            print(reponse)
            if "[" in reponse and "]" in reponse :
                print("Le LLM a besoin de plus d'informations pour completer la réponse.")
                while "[" in reponse and "]" in reponse:
                    start = reponse.index("[")
                    end = reponse.index("]", start)
                    placeholder = reponse[start:end+1]
                    user_input = input(f"{placeholder} : ") # Demande à l'utilisateur de compléter l'info manquante si besoin
                    reponse = reponse.replace(placeholder, user_input, 1)
            print(reponse)
            print("Mail prêt à l'envoi, envoyer ? (O/N)")
            send = input() # Demande à l'utilisateur si l'email lui convient
            if send.lower() == "o":
                load_dotenv()
                print("Envoi du mail...")
                send_email(mail["Envoyeur :"].split("<")[1].strip(">"), "Re:"+ mail["Sujet :"], reponse, os.getenv("EMAIL_ACCOUNT"), os.getenv("EMAIL_PASSWORD"))
                print("Mail envoyé !")

            


        time.sleep(30) # Pause de 30 secondes avant de chacker à nouveau les nouveaux emails
        print("Vérification des nouveaux mails...")



if __name__ == "__main__":
    main()
