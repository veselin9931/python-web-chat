import chainlit as cl
from llama_cpp import Llama
import time
import asyncio

MODEL_PATH = "./models/bggpt-gemma-2-2.6b-it-v1.0-q8_0.gguf"
# MODEL_PATH = "./models/BgGPT-Gemma-2-27B-IT-v1.0.i1-IQ1_S.gguf"
# MODEL_PATH = "./models/BgGPT-Gemma-2-9B-IT-v1.0.i1-Q4_K_S.gguf"

try:
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=2048,
        n_batch=512,
        verbose=True,
    )
except Exception as e:
    print(f"Model lo ading error: {e}")
    llm = None

@cl.on_chat_start
async def start():
    if llm is None:
        await cl.Message(content="❌ Неуспешно зареждане на модела. Проверете пътя до модела.").send()
    else:
        await cl.Message(content="🤖 Моделът е готов!").send()
        await cl.Message(content="👋 Добре дошъл в чат асистента на Уникредит Булбанк! С какво да помогна?", ).send()




async def update_timer(message):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        await message.update(content=f"⏳ Генериране на отговор... ")
        await asyncio.sleep(0.1)

@cl.on_message
async def main(message: cl.Message):
    if llm is None:
        await cl.Message(content="Моделът не е зареден. Не мога да обработя заявката ви.").send()
        return

    # Създаваме първоначално съобщение
    msg = cl.Message(content=f"⏳ Генериране на отговор...")
    await msg.send()

    try:
        start_time = time.time()
        
        output = await asyncio.to_thread(
            llm,
            prompt=f"\n### Q:\n{message.content}\n### A:\n",
            max_tokens=500,  # Увеличен брой tokens
            stop=["\n", "###"],
            echo=False
        )
        

        response = output["choices"][0]["text"].strip()
        elapsed_time = time.time() - start_time
        
        print(f"{response}\n\n⏱️ Време за генериране: {elapsed_time:.2f} секунди")

        # Създаваме ново съобщение вместо да обновяваме старото
        await cl.Message(content=f"{response}\n\n⏱️ Време за генериране: {elapsed_time:.2f} секунди").send()
        
        # Премахваме съобщението за зареждане
        await msg.remove()
        
    except Exception as e:
        await msg.remove()
        await cl.Message(content=f"Грешка при генериране на отговор: {e}").send()