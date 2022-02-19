from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site= input("Please paste the scientific paper here: ") #"https://www.sciencedirect.com/science/article/pii/S0043135402004967"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
#print(soup)

mytext = soup.find("div", {"id": "abstracts"}).text

from gtts import gTTS

language = 'en'
accent = 'com'
accent_input = input("Please select an English accent (Australia, United Kingdom, United States, Canada, India, Ireland, South Africa): ")
if accent_input == "Australia":
    accent = "com.au"
if accent_input == "United Kingdom":
    accent = "co.uk"
if accent_input == "United States":
    accent = "com"
if accent_input == "Canada":
    accent = "ca"
if accent_input == "India":
    accent = "co.in"
if accent_input == "Ireland":
    accent = "ie"
if accent_input == "South Africa":
    accent = "co.za"

myobj = gTTS(text=mytext, lang=language, tld=accent, slow=False)
filename = "filename.mp3"
myobj.save(filename)

print("Successful! Please enjoy listening to your science buddy :)")