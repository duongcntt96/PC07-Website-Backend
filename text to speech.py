# Import the required module for text 
# to speech conversion
from gtts import gTTS
import os
mytext = 'Xin chào'
language = 'vi'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")