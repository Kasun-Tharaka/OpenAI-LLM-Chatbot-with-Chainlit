import chainlit as cl
from src.llm import ask_details, messages

@cl.on_message
async def main(message: cl.Message):
    # Custom logic
    ##append to messages user input or ask questions
    messages.append({'role': 'user', 'content': message.content})
    response = ask_details(messages)
    ##appending the response
    messages.append({'role': 'assistant', 'content': response})

    # Send response back to user / front end UI
    await cl.Message(
        content=response,
    ).send()