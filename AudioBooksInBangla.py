from gtts import gTTS
import playsound
import os

tts= gTTS(text='আমার বই', lang='bn')
tts.save("mybook.mp3")
os.system("mpg321 mybook.mp3")
playsound.playsound('mybook.mp3',True)