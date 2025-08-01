from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
print(f"API key: {key}")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)

completion = client.chat.completions.create(
  
  extra_body={},    
  model="google/gemma-3n-e4b-it:free",
  temperature=0.9,
  max_tokens=100,   
  messages=[
    { "role": "system",
      "content": "You are a specialized email response assistant. Your task is to provide an optimised and personalized human-like response to the email given by the user.",
      "role": "user",
      "content": "Bonjour Baptiste, Je fais suite a nos échanges , je ne sais pas si tu as une facture acquittée de ton dentiste si oui il faudrait me l'envoyer pour que je puisse la transmettre a Henner. bonne soirée."
    }
  ]

)
print(completion)
print(completion.choices[0].message.content)