#converting text audio using python 

from gtts import gTTS # we are importing gtts 
from playsound import playsound
audio="speech.mp3"
language="en"
sp=gTTS(text="vande mataram, vande mataram sujalaam suphalaam ",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("======audio is playing.....")


