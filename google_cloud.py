from curses.ascii import US
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from google.cloud import texttospeech

# site= input("Please paste the scientific paper here: ") #"https://www.sciencedirect.com/science/article/pii/S0043135402004967"
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(site,headers=hdr)
# page = urlopen(req)
# print(site)
# soup = BeautifulSoup(page)
# abstract = soup.find("div", {"id": "abstracts"}).text
# print(abstract)

def get_abstract(site):
    #site= input("Please paste the scientific paper here: ") #"https://www.sciencedirect.com/science/article/pii/S0043135402004967"
    #site = "https://www.science.org/doi/10.1126/science.1255057"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    #print(site)
    soup = BeautifulSoup(page)
    abstract = soup.find("div", {"id": "abstracts"}).text
    #print(abstract)
    return abstract

def text_to_speech(abstract, accent, speed):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=abstract)

    accent_code = "en-US"
    #accent_input = input("Please select an English accent (United States, Australia, United Kingdom, India): ")
    if accent == "Australia":
        accent_code = "en-AU"
    if accent == "United Kingdom":
        accent_code = "en-GB"
    if accent == "India":
        accent_code = "en-IN"

    rate = 1
    #rate_input = input("Please enter slow, regular, or fast for speaking rate: ")
    if speed == "slow":
        rate = 0.5
    if speed == "fast":
        rate = 1.5

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code=accent_code, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=rate
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    # The response's audio_content is binary.
    with open("gcloud_abstract.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        #print('Audio content written to file "gcloud_abstract.mp3"')
    # return "gcloud_abstract.mp3"
    
    # return abstract