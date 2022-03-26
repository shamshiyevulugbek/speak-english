import requests
word = input("Inglizcha so'z yozing :")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
r = requests.get(url)
print(r.status_code)
try:
    meanings = r.json()[0]["meanings"]
    audio_url = r.json()[0]["phonetics"][1]['audio']
except:
    print(r.json()['message'])
else:
    for i in meanings:
        print(f"***{i['partOfSpeech'].upper()}***")
        for j in i["definitions"]:
            print(j["definition"])
