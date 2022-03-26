from googletrans import Translator
import requests
my_text = input("my_text :")
translator = Translator()
translated = translator.translate(my_text)
new_text = translated.text
word_len = len(new_text.split())
if word_len != 1:
    if translated.src == "en":
        uz_text = translator.translate(new_text,dest="uz").text
        print(uz_text)
    else:
        print("Matn tili inglizcha emas :",translated.src)
        print(new_text)
else:
    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{new_text}"
    r = requests.get(URL)
    print(new_text)
    try:
        meanings = r.json()[0]["meanings"]
        print("manoga yeti keldik")
        audio_url = r.json()[0]["phonetics"][0]['audio']
        print("audioga yetib keldik")
    except:
        print("👉 indefinite word")
        print(r.json()["message"])
        print("xatolik tepada bor")
    else:
        matn = ""
        for i in meanings:
            matn += f"🔥🔥🔥{i['partOfSpeech'].upper()}🔥🔥🔥\n"
            for j in i["definitions"]:
                matn +="✔️" + j["definition"] + "\n"
            print(matn)
        if audio_url:
            print(audio_url)
