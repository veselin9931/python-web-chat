import chainlit as cl

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Добре дошъл в чат асистента на Уникредит Булбанк! С какво да помогна?",
    ).send()

@cl.on_message
async def main(message: cl.Message):
    try:
        response = f"Вие попитахте: {message.content}"
        await cl.Message(content=response).send()
    except Exception as e:
        await cl.Message(
            content=f"An error occurred: {str(e)}"
        ).send()