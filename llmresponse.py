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
        "content": "You are a specialized email response assistant. Your task is to provide an optimised and personalized human-like response to the email given by the user. The email is given to you in a dictionary format with first the subject, then the sender, then the body of the email and finally the attachments if there are any. You must only return the response, and only the response, no suggestion or anything else. Here is the email information :"
        + str (mail_info)

        }]
    


    completion = client.chat.completions.create(
    extra_body={},    
    model="google/gemma-3n-e4b-it:free",
    temperature=0.9,
       
    messages=prompt
    )

    return completion.choices[0].message.content

