from gtts import gTTS
import os

# Текст, который нужно озвучить
text = "Привет, мир!"

# Создание объекта gTTS с указанием текста и языка (Russian)
tts = gTTS(text=text, lang='ru')

# Сохранение озвученного текста в файл
tts.save("output.mp3")

# Воспроизведение озвученного текста
os.system("start output.mp3")
