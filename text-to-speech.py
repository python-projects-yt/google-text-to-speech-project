from gtts import gTTS
import os
mytext="hello world I am a good boy "
language="fr"
output=gTTS(text=mytext,lang=language)
output.save("intro.mp3")
os.system("start intro.mp3")