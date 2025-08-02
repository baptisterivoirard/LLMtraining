from openai import OpenAI
import os
from dotenv import load_dotenv


def reponse_llm (mail_info):
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")



    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
    )

    prompt = [{ "role": "system",
        "content":  "You are a specialized email response assistant. Your goal is to write clear, professional, and human-like replies to emails." +
    " The user provides you with the full content of an email in dictionary format (subject, sender, body, attachments)." +
    "\n\nIf the email requires subjective input or contextual knowledge that you do not have (for example: opinions, decisions, or specific status updates)," +
    " you MUST insert a placeholder in the response like: [Add your opinion on the product here] or [Specify your availability here] that is asking for the information you don't know." +
    "\n\nIf you do have enough context to reply meaningfully, go ahead and write the complete response directly." +
    "\n\nDo not explain your reasoning. Only return the email response." +
    "\n\nHere is the email information:\n" 
    + str(mail_info)

        }]
    


    completion = client.chat.completions.create(
    extra_body={},    
    model="google/gemma-3n-e4b-it:free",
    temperature=0.9,
       
    messages=prompt
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    test_mail = {'Sujet :': 'Demande de rendez-vous pour un échange sur votre projet', 'Envoyeur :': 'Baptiste Rivoirard <rivoirardbaptiste2@gmail.com>', 'Corps :': 'Bonjour,\r\n\r\nJe me permets de vous contacter pour convenir d’un rendez-vous afin de\r\ndiscuter de votre projet en cours. Seriez-vous disponible cette semaine\r\npour un échange rapide par téléphone ou visioconférence ?\r\n\r\nBien cordialement,\r\nClaire Dupuis\r\n', 'pièces jointes : ': {}}
    print(reponse_llm(test_mail))