import logging
import requests
from googletrans import Translator

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5143455912:AAGQ14RDzL5BA0uOgN-hkahJ7iqaOu_Y6lw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# @db.ge_handler(commands=['help'])
# async def help_buyruq(buyruq:types.Message):
#     await buyruq.answer("Ixtiyoriy tilga tegishli bo'lgan matn yoki so'z kiriting!")
@dp.message_handler(commands=['start,help'])
async def hammaga_salom(xabar: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await xabar.reply("Assalomu alaykum!\nShamshiye Ulug'bekning ingliz tili botiga xush kelibsiz!\nBoshlash uchun /start buyrug'ini kiriting!")
    
@dp.message_handler()
async def tarjima(salom: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    #SHU YERGA ASOSIY DASTURNI YOZAMIZ
    translator = Translator()
    translated = translator.translate(salom.text)
    new_text = translated.text
    word_len = len(new_text.split())
    if word_len != 1:
        if translated.src == "en":
            uz_text = translator.translate(new_text,dest="uz").text
            await salom.reply(uz_text)
        else:
            await salom.reply(new_text)
    else:
        URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{new_text}"
        r = requests.get(URL)
        try:
            meanings = r.json()[0]["meanings"]
            audio_url = r.json()[0]["phonetics"][0]['audio']
        except:
            await salom.reply("👉 indefinite word")
            await salom.answer(r.json()["message"])
        else:
            matn = ""
            for i in meanings:
                matn += f"🔥🔥🔥{i['partOfSpeech'].upper()}🔥🔥🔥\n"
                for j in i["definitions"]:
                    matn +="✔️" + j["definition"] + "\n"
            await salom.answer(matn)
            if audio_url:
                await salom.reply_audio(audio_url)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)