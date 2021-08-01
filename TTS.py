
#NOTE:Insert Importing library

pip install ibm_watson
pip install ibm_cloud_sdk_core


from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Insert API Key in place of 
# 'YOUR UNIQUE API KEY'
api = IAMAuthenticator("YOUR UNIQUE API KEY")
text_2_speech = TextToSpeechV1(
    authenticator=api
)

#Insert URL in place of 'API_URL' 
text_2_speech.set_service_url("API_URL")

# Recognize text using IBM Text to Speech

with open("Testing-TTS.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize("Hello, Testing text to speech service",accept="audio/mp3").get_result().content)

    # write the content to the audio file
    # Save TTS as mp3 file