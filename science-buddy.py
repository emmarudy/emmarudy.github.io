# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import requests

website = input("Please paste the doi link here")
mytext = requests.get(website)
mytext.text

# The text that you want to convert to audio
# https://www.sciencedirect.com/science/article/pii/S0043135402004967

#mytext = "Abstract In July 1999, California's ocean recreational bacterial water quality standards were changed from a total coliform (TC) test to a standard requiring testing for all three bacterial indicators: TC, fecal coliforms (FC), and enterococci (EC). To compare the relationship between the bacterial indicators, and the effect that changing the standards would have on recreational water regulatory actions, three regional studies were conducted along the southern California shoreline from Santa Barbara to San Diego, California. Two studies were conducted during dry weather and one following a large storm event. In each study, samples were collected at over 200 sites which were selected using a stratified random design, with strata consisting of open beach areas and rocky shoreline, and areas near freshwater outlets that drain land-based runoff. During the dry weather studies, samples were collected once per week for 5 weeks. For the storm event study, sampling occurred on a single day about 24 h following the storm. The three indicator bacteria were measured at each site and the results were compared to the single sample standards (TC>10,000; FC>400 and EC>104 MPN or cfu/100 ml). EC was the indicator that failed the single sample standards most often. During the wet weather study, 99% of all standard failures were detected using EC, compared with only 56% for FC, and 40% for TC. During the Summer Study, EC was again the indicator that failed the single sample standards most often, with 60% of the failures for EC alone. The increased failure of the EC standard occurred consistently regardless of whether the sample was collected at a beach or rocky shoreline site, or at a site near a freshwater outlet. Agreement among indicators was better during wet weather than during dry weather. During dry weather, agreement among indicators was better near freshwater outlets than along open shoreline. Cumulatively, our results suggest that replacement of a TC standard with an EC standard will lead to a five-fold increase in failures during dry weather and a doubling of failures during wet weather. Replacing a TC standard with one based on all three indicators will lead to an eight-fold increase in failures. Changes in the requirements for water quality testing have strong implications for increases in beach closures and restrictions."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("test_abstract.mp3")

# Playing the converted file
os.system("mpg321 noble.mp3")