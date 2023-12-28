from openai import OpenAI
from src.prompt import instruction

client = OpenAI

messages = [
    {'role': 'system', 'content': instruction}
]

#here also you can use open source LLM with LangChain

def ask_details(message, model="gpt-3.5-turbo", template=0):
    response = client.chat.completetion.create(
        model=model,
        message = message,
        template=template
        )
    
    return response.choice[0].message.content