import imaplib
import email
from email.header import decode_header
import sys 
import time
import os
from dotenv import load_dotenv
from emailrecup import email_recup

def main ():
    while True:
        list_mails=[]
        list_mails=email_recup()
        print(list_mails)
        

        time.sleep(60)



if __name__ == "__main__":
    main()
