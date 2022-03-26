# from googletrans import Translator
# translator = Translator()
# a = translator.translate('Assalomu alaykum')
# a bu yerda tarjima qilingan obekt.
# tarjima matni a.text
# tarjima qilinishi kerak matn tili a.src
# tarjima qlingan matn tili a.dest 
#Biz qaysi tilga tarjima qilishni ham berishimiz mumkin:
# a = translator.translate(text,dest = 'uz') 


# from googletrans import Translator
# translator = Translator()
# a = translator.detect('Assalomu alaykum')
# print(a)
# print(a.lang)
# Detected(lang=uz, confidence=0.9490306)
# uz

from googletrans import Translator

t = Translator()
a = input("Text :")
b = t.translate(a)
print(b.text)
print(b.src)
print(b.dest)