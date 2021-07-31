
#NOTE: Importing library 

!pip install ibm_watson

!pip install SpeechRecognition

!pip install pipwin

#Install pyaudio because it uses the Microphone class

!pipwin install pyaudio

#Open Speech to Text service

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'LLHuzhS2w1dV4T6PvXnx1k52uS8xtq9I6tyhyh4DQPGM'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/ff6092c3-b3b3-4749-ad7e-80b80b39e3aa'

# Setup Service

authenticator =IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

#SpeechRecognition module supports multiple recognition API

import speech_recognition as sr

#Create a Recognizer

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)

#Recognize Speech

with mic as source: 
  audio = r.listen(source) 
result = r.recognize_google(audio)
print(result)

#Exporting the result
with open('myresult.txt',mode ='w') as file: 
   file.write("Recognized text:") 
   file.write("\n") 
   file.write(result) 
print("Exporting process completed!")