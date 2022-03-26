import requests
from pprint import pprint 


TOKEN ='749932d3134d77d542a96e5b'

pair1 = 'USD'
pair2 = 'UZS'

URL = f"https://v6.exchangerate-api.com/v6/{TOKEN}/pair/{pair1}/{pair2}"
URL2 = "https://api.pray.zone/v2/times/tomorrow.json?city=mecca&school=2"
payground = {'city':'mecca','school':'2'}

res = requests.get("https://api.pray.zone/v2/times/tomorrow.json",params=payground)

print(res.status_code)
print(res.url)
print(res.text)
print(res.encoding)
print(res.content)




