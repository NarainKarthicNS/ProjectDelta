import pyttsx3#text to speech conversion library
import datetime #To get all data related to date time 
import speech_recognition as sr #Speech to text conversion library
import wikipedia #to get data from wikipedia API
import webbrowser #To open website on the web
import os #To Operate System Function Such a Saving As Well As Power Controls
import wolframalpha #To get answer to questions from wolfram alpha ai algorithms
import pyjokes  #To get jokes relating to programming 
import ecapture as ec #To capture photo through webcam
import winshell #To process Recycle bin and other functions
import AppOpener #To open applications hands off
import python_weather #To get accurate weather predictions
import asyncio #To Use async methods for weather module
import json #To get user data
from urllib.request import urlopen #To process user data
from pydictionary import Dictionary #TO do all dictionary functions
from translate import Translator #To Translate languages
from pytube import YouTube #To download YT videos and extract audio from them
from tkinter import Tk #To access filedialouge box gui
from tkinter.filedialog import askopenfilename #To ask to open a file through gui
import pyautogui #To take ScreenShots and Other GUI functions
import time #To access time related functions
from gnews import GNews #To get top headlines and genre based news




#Initializing Parameters
engine = pyttsx3.init('sapi5')#sapi5 is microsoft's  Speech Application Programming Interface  
voices = engine.getProperty('voices')
engine. setProperty("rate", 185)
engine.setProperty('voice' , voices[6].id)
# print(voices[6].id)
webbrowser.register('google-chrome', None)
google_news = GNews()

#defining the functions of speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wish the user according to time of the day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Narain" )
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Narain")

    else:
        speak("Good Evening Narain")
    
    speak("How may I assist you?")

def Listen():
    #Takes a command through microphone and converts it to a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
     
    print("Recognizing...")
    baseQuery = r.recognize_google(audio)
    print(f"User Said: {baseQuery}\n")

   

    return baseQuery

def takeCommand():
    #Takes a command through microphone and converts it to a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("could you please repeat")
        speak("I did not catch that , could you please repeat")
        return "None"

    return query

#Get Location Data to process & access weather forecast 
def getLocationData():
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    return city

# Get Weather Forecast data through "python_weather" module
async def getweather(city):
    print("Searching...")
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        if city.lower() == "my location" or city.lower() == "current location":
            city = getLocationData()

        weather = await client.get(city)

        temperature = weather.current.temperature
        speak("Search complete! , According to my database")
        print(f"Temperature at {city} --> {temperature}°F")
        speak(f"The current Temperature at {city} is around {temperature} degree fahrenheit")

        fl = weather.current.feels_like       
        description = weather.current.description
        humidity = weather.current.humidity
        
        
        print(f"It feels like an average temperature of {fl}°F")
        speak(f"It feels like an average temperature of {fl} degree fahrenheit")       
        print(f"Today can be described as {description.upper()} day with a humidity level of {humidity}")
        speak(f"Today can be described as {description} day with a humidity level of {humidity}")
        if "rain" in description.lower():
            print("--> I WOULD ADVISE YOU TO CARRY AN UMBRELLA")
            speak("I would advise you to carry an umbrella")
        elif "cloudy" in description.lower():
            print("--> I WOULD ADVISE YOU TO STAY IN HOME IF YOU HAVE COMMON COLD")
            speak("I would advise you to stay in home if you have common cold")
        elif "sunny"  in description.lower():
            print("--> I WOULD ADVISE YOU TO GO OUT AND ENJOY THE DAY , SUNNY DAYS CAN HELP YOU WITH VITAMIN D")
            speak("I would advise you to go out and enjoy the day , sunny days can help you with vitamin D")
        elif "clear"  in description.lower():
            print("--> Well , All I can say is today we have a pleasant weather !")
            speak("Well , All I can say is today we have a pleasant weather !")
        print("Here are the ASTRONOMY and HOURLY weather forecast details available currently")
        speak("here are the astronomy and hourly weather forecast details available currently")
        for forecast in weather.forecasts:
            print("ASTRONOMY --> " , forecast.date , forecast.astronomy)
            for hourly in forecast.hourly:
                
                print(f"--> {hourly!r}")

#TO search DataBase through WOlframAlpha AI
def searchDatabase(Q):
    app_id = 'VJRU4R-4YXR4Y5YV2'
    client = wolframalpha.Client(app_id)
    res = client.query(Q)
    answer = next(res.results).text
    if answer != None:
        print(answer)
        speak(answer)
    else:
        speak("I currently don't have any information regarding that!")

#To get word meaning using Dictionary Module
def getMeaning(word):
    dict = Dictionary(word)
    meaning = dict.meanings()
    dict.print_meanings("blue")
    speak(meaning)

#To get word synonym using Dictionary Module

def getSynonym(word):
    dict = Dictionary(word)
    synonym = dict.synonyms()
    dict.print_synonyms("green")
    speak(f"synonyms of{word} include {synonym}")

#To get word antonym using Dictionary Module
def getAntonym(word):
    dict = Dictionary(word)
    antonym = dict.antonyms()
    dict.print_antonyms("red")
    speak(f"antonyms of{word} include {antonym}")




#Language Codes
ISO639 = {
    "Abkhazian":"ab",
    "afar" :"aa",
    "afrikaans":"af",
    "akan":"ak",
    "albanian":"sq",
    "amharic":"am",
    "arabic":"ar",
    "aragonese":"an",
    "armenian":"hy",
    "assamese":"as",
    "avaric":"av",
    "avestan":"ae",
    "aymara":"ay",
    "azerbaijani":"az",
    "bambara":"bm",
    "bashkir":"ba",
    "basque":"eu",
    "belarusian":"be",
    "bengali":"bn",
    "bislama":"bi",
    "bosnian":"bs",
    "breton":"br",
    "bulgarian":"bg",
    "burmese":"my",
    "catalan":"ca",
    "central khmer	":"km",
    "chamorro":"ch",
    "chechen":"ce",
    "chichewa":"ny",
    "chinese":"zh",
    "church slavonic":"cu",
    "chuvash":"cv",
    "cornish":"kw",
    "corsican":"co",
    "cree":"cr",
    "croatian":"hr",
    "czech":"cs",
    "danish":"da",
    "divehi":"dv",
    "dutch":"nl",
    "dzongkha":"dz",
    "english":"en",
    "esperanto":"eo",
    "estonian":"et",
    "ewe":"ee",
    "faroese":"fo",
    "fijian":"fj",
    "finnish":"fi",
    "french":"fr",
    "fulah":"ff",
    "gaelic":"gd",
    "galician":"gl",
    "ganda":"lg",
    "georgian":"ka",
    "german":"de",
    "greek	":"el",
    "guarani":"gn",
    "gujarati":"gu",
    "haitian":"ht",
    "hausa":"ha",
    "hebrew":"he",
    "herero":"hz",
    "hindi":"hi",
    "hiri motu":"ho",
    "hungarian":"hu",
    "icelandic":"is",
    "ido":"io",
    "igbo":"ig",
    "indonesian":"id",
    "interlingua":"ia",
    "interlingue":"ie",
    "inuktitut":"iu",
    "inupiaq":"ik",
    "irish":"ga",
    "italian":"it",
    "japanese":"ja",
    "javanese":"jv",
    "kalaallisut":"kl",
    "kannada":"kn",
    "kanuri":"kr",
    "kashmiri":"ks",
    "kazakh":"kk",
    "kikuyu":"ki",
    "kinyarwanda":"rw",
    "kirghiz":"ky",
    "komi":"kv",
    "kongo":"kg",
    "korean":"ko",
    "kuanyama":"kj",
    "kurdish":"ku",
    "lao":"lo",
    "latin":"la",
    "latvian":"lv",
    "limburgan":"li",
    "lingala":"ln",
    "lithuanian":"lt",
    "luba katanga":"lu",
    "letzeburgesch":"lb",
    "macedonian":"mk",
    "malagasy":"mg",
    "malay":"ms",
    "malayalam":"ml",
    "maltese":"mt",
    "manx":"gv",
    "maori":"mi",
    "marathi":"mr",
    "marshallese":"mh",
    "mongolian":"mn",
    "nauru":"na",
    "navajo":"nv",
    "ndonga":"ng",
    "nepali":"ne",
    "north ndebele":"nd",
    "northern sami":"se",
    "norwegian":"no",
    "norwegian bokmal":"nb",
    "norwegian nynorsk":"nn",
    "occitan":"oc",
    "ojibwa":"oj",
    "oriya":"or",
    "oromo":"om",
    "ossetian":"os",
    "pali":"pi",
    "pashto":"ps",
    "persian":"fa",
    "polish":"pl",
    "portuguese":"pt",
    "punjabi":"pa",
    "quechua":"qu",
    "romanian":"ro",
    "romansh":"rm",
    "rundi":"rn",
    "russian":"ru",
    "samoan":"sm",
    "sango":"sg",
    "sanskrit":"sa",
    "sardinian":"sc",
    "serbian":"sr",
    "shona":"sn",
    "sichuan":"yi",
    "sindhi":"sd",
    "sinhala":"si",
    "slovak":"sk",
    "slovenian":"sl",
    "somali":"so",
    "south ndebele":"nr",
    "southern sotho":"st",
    "spanish":"es",
    "sundanese":"su",
    "swahili":"sw",
    "swati":"ss",
    "swedish":"sv",
    "tagalog":"tl",
    "tahitian":"ty",
    "tajik":"tg",
    "tamil":"ta",
    "tatar":"tt",
    "telugu":"te",
    "thai":"th",
    "tibetan":"bo",
    "tigrinya":"ti",
    "tonga":"to",
    "tsonga":"ts",
    "tswana":"tn",
    "turkish":"tr",
    "turkmen":"tk",
    "twi":"tw",
    "uighur":"ug",
    "ukrainian":"uk",
    "urdu":"ur",
    "uzbek":"uz",
    "venda":"ve",
    "vietnamese	":"vi",
    "volapuk	":"vo",
    "walloon	":"wa",
    "welsh	":"cy",
    "western frisian":"fy",
    "wolof":"wo",
    "xhosa":"xh",
    "yiddish":"yi",
    "yoruba":"yo",
    "zhuang":"za",
    "zulu":"zu"

}

#To translate from ENG to 185+ ISO639 Verified Languages
def translate(to_lang):
    lang = ISO639[to_lang.lower()]
    translator= Translator(to_lang=lang)
    sentence = input("Sentence/Phrase/Word : ")
    translation = translator.translate(sentence)
    print("Translating...")
    speak("Translating")    
    print(translation)

#Download YouTube Video 
def DownloadVideo(url):
    yt = YouTube(url)
    title = yt.title
    views = yt.views
    print("Title : " ,title)
    print("Views : " , views)
    print("Thumbnail : " ,yt.thumbnail_url)
    print("Downloading...")
    speak(f"Requesting my database to download ,{title} video")
    stream = yt.streams.get_by_itag(22)
    path = os.getcwd()
    dir = path + "\YoutubeDownloads"
    stream.download(output_path= dir)
    print("--> Download Complete")
    speak("Dowload Complete")
    title = title.replace("." , "")
    file = dir + "\\" + title + ".mp4"    
    speak("Your file can be found in below location")
    print("Your file can be found in below location")
    os.startfile(file)
    print(file)

#Extract Audio From YouTube Video
def DownloadAudio(url):
    yt = YouTube(url)
    title = yt.title
    print("Title : " ,title)
    audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    print("Extracting...")
    speak(f"Requesting my database to extract audio from ,{title} video")
    path = os.getcwd()
    dir = path + "\AudioDownloads"
    audio.download(output_path= dir)
    print("--> Extraction Complete")
    speak("Extraction Complete")
    title = title.replace("." , "")
    file = dir + "\\" + title + ".mp4" 
    newFile = dir + "\\" + title + ".mp3" 
    os.rename(file,newFile)
    speak("Your file can be found in below location")
    print("Your file can be found in below location")
    os.startfile(newFile)
    print(newFile)

#Convert FileType from one type to another  
def convertFileType(fromType , ToType):
    speak("Select the file you want to convert,")
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    speak(f"Requestion my Database to convert your file , from {fromType} to {ToType}")
    print("File Name : " + filename)
    filename.replace(fromType , "")
    newFileName = filename + ToType
    os.rename(filename , newFileName )
    os.startfile(newFileName)
    print("Done Converting")
    speak("Your File type has been converted and your older file replaced by your requestion formatted file")

#Capture Whole Screen Using PyAutoGui Module
def screenShot():
    print("Capturing your screen in 3s...")
    speak("Capturing your screen in 3 seconds")
    time.sleep(1)
    print("-3-")
    speak("3")
    time.sleep(1)
    print("-2-")
    speak("2")
    time.sleep(1)
    print("-1-")
    speak("1")
    ScreenCapture = pyautogui.screenshot()
    print("Screen Captured...")
    speak("Screen Captured")
    speak("input your filename below , giving an existing file name might override your previous files")
    fileName = input("Save As : ")
    FormattedFileName = fileName + ".png"
    path = os.getcwd()
    dir = path + "\ScreenCapture\\"
    file = dir + FormattedFileName
    ScreenCapture.save(file)
    speak("Here is your screenshot")
    os.startfile(file)

#Snip Parts of Screen Using Windows Builtin Snip Tool
def snip():
    print("Opening Screen Snip in 3s...")
    speak("Opening Screen Snip in 3 seconds")
    time.sleep(1)
    print("-3-")
    speak("3")
    time.sleep(1)
    print("-2-")
    speak("2")
    time.sleep(1)
    print("-1-")
    speak("1")
    pyautogui.hotkey('win' , 'shift' , 's') 
    
#Get Top Headlines using GoogleNews
def getTopNews():
    print("Searching...")
    topNews = google_news.get_top_news()
    print("======Top Headlines======")
    speak("Here are the top headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")
    
    speak("You Can Also Access Headlines of Specific Genres mention below")
    print("You Can Also Access Headlines of Specific Genres including :")
    print("WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH.")

#Get Tech Headlines using GoogleNews
def getTechNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("TECHNOLOGY")
    print("======Top Tech Headlines======")
    speak("Here are the top tech headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get Science Headlines using GoogleNews   
def getScienceNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("SCIENCE")
    print("======Top Science Headlines======")
    speak("Here are the top science headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get Health Headlines using GoogleNews
def getHealthNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("HEALTH")
    print("======Top Health Headlines======")
    speak("Here are the top health headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get Sports Headlines using GoogleNews   
def getSportsNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("SPORTS")
    print("======Top Sports Headlines======")
    speak("Here are the top sports headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get International Headlines using GoogleNews
def getWorldNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("WORLD")
    print("======Top International Headlines======")
    speak("Here are the top world headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get National Headlines using GoogleNews  
def getNationNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("NATION")
    print("======Top National Headlines======")
    speak("Here are the top national headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get Business Headlines using GoogleNews
def getBusinessNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("BUSINESS")
    print("======Top Business Headlines======")
    speak("Here are the top business headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#Get Entertainment Headlines using GoogleNews   
def getEntertainmentNews():
    print("Searching...")
    topNews = google_news.get_news_by_topic("ENTERTAINMENT")
    print("======Top Entertainment Headlines======")
    speak("Here are the top entertainment headlines i gathered , ")
    for i in topNews:
        headline = i.get("title")
        index = topNews.index(i)
        num = index + 1
        print(str(num) + " - " + headline)
        if num < 5:
            speak(headline)
        elif num == 5:
            speak(headline + "and so on")

#ShutDown PC using OS Module and os.system function
def shutdown ():
    speak("Do You Wish To ShutDown Your PC ? You Could Lose Your Unsaved Work")
    print("Do You Wish To ShutDown Your PC ? You Could Lose Your Unsaved Work")
    newQuery = Listen().lower()
    if "yes" in newQuery or "yup" in newQuery or "yeah" in newQuery or "yea" in newQuery:
        print("Shutting down your pc in 10s...")
        speak("Shutting down your pc in 10 seconds")
        time.sleep(1)
        print("-10-")
        speak("10")
        time.sleep(1)
        print("-9-")
        speak("9")
        time.sleep(1)
        print("-8-")
        speak("8")
        time.sleep(1)
        print("-7-")
        speak("7")
        time.sleep(1)
        print("-6-")
        speak("6")
        time.sleep(1)
        print("-5-")
        speak("5")
        time.sleep(1)
        print("-4-")
        speak("4")
        time.sleep(1)
        print("-3-")
        speak("3")
        time.sleep(1)
        print("-2-")
        speak("2")
        time.sleep(1)
        print("-1-")
        speak("1")
        os.system("shutdown /s /t 3")
        exit()
    else:
        speak("Ok")

#Restart PC using OS Module and os.system function
def restart():
    speak("Do You Wish To Restart Your PC ? You Could Lose Your Unsaved Work")
    print("Do You Wish To Restart Your PC ? You Could Lose Your Unsaved Work")
    newQuery = Listen().lower()
    if "yes" in newQuery or "yup" in newQuery or "yeah" in newQuery or "yea" in newQuery:
        print("Restarting your pc in 10s...")
        speak("Restarting your pc in 10 seconds")
        time.sleep(1)
        print("-10-")
        speak("10")
        time.sleep(1)
        print("-9-")
        speak("9")
        time.sleep(1)
        print("-8-")
        speak("8")
        time.sleep(1)
        print("-7-")
        speak("7")
        time.sleep(1)
        print("-6-")
        speak("6")
        time.sleep(1)
        print("-5-")
        speak("5")
        time.sleep(1)
        print("-4-")
        speak("4")
        time.sleep(1)
        print("-3-")
        speak("3")
        time.sleep(1)
        print("-2-")
        speak("2")
        time.sleep(1)
        print("-1-")
        speak("1")
        os.system("shutdown /r /t 3")
        exit()
    else:
        speak("Ok")
#Logout PC using OS Module and os.system function
def logout():
    speak("Do You Wish To Logout Your PC ? You Could Lose Your Unsaved Work")
    print("Do You Wish To Logout Your PC ? You Could Lose Your Unsaved Work ")
    newQuery = Listen().lower()
    if "yes" in newQuery or "yup" in newQuery or "yeah" in newQuery or "yea" in newQuery:
        print("Logging Out your pc in 5s...")
        speak("Logging Out your pc in 5 seconds")
        time.sleep(1)
        print("-5-")
        speak("5")
        time.sleep(1)
        print("-4-")
        speak("4")
        time.sleep(1)
        print("-3-")
        speak("3")
        time.sleep(1)
        print("-2-")
        speak("2")
        time.sleep(1)
        print("-1-")
        speak("1")
        os.system("shutdown -l ")
        exit()
    else:
        speak("Ok")

#Hibernate PC using OS Module
def sleepPC ():
    speak("Do You Wish To Put Your PC to Sleep ? ")
    print("Do You Wish To Put Your PC to Sleep ?")
    newQuery = Listen().lower()
    if "yes" in newQuery or "yup" in newQuery or "yeah" in newQuery or "yea" in newQuery:
        print("Suspending your pc in 5s...")
        speak("Suspending your pc in 5 seconds")
        time.sleep(1)
        print("-5-")
        speak("5")
        time.sleep(1)
        print("-4-")
        speak("4")
        time.sleep(1)
        print("-3-")
        speak("3")
        time.sleep(1)
        print("-2-")
        speak("2")
        time.sleep(1)
        print("-1-")
        speak("1")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        exit()
    else:
        speak("Ok")



if __name__ == "__main__":
    baseQuery = Listen().lower()
    if "activate" in baseQuery:

        print("Activating delta , your personal companion")
        speak("Activating Project delta , your personal companion")
        wishme()
        while True:

            query = takeCommand().lower()
            #Logic for executing tasks based on query

            if "who are you" in query:
                speak("I am delta - your personal companion")

            elif "what does delta stand for" in query:
                speak("delta stands for Dynamic Executable Logic Based Technological Assistant")
                print("delta stands for Dynamic Executable Logic Based Technological Assistant")
            
            elif "what is love" in query:
                print("Even though i can't feel emotion , Love is the chemical defect found in the losing side and it is defined as the 7th sense , that occludes other senses from working")
                speak("Even though i can't feel emotion , Love is the chemical defect found in the losing side and it is defined as the 7th sense , that occludes other senses from working")
            
            elif  "wikipedia" in query:
                query = query.replace("wikipedia"  , "")
                query = query.replace("search"  , "")
                query = query.replace("for"  , "")
                query = query.replace("hey"  , "")
                query = query.replace("delta"  , "")
                query = query.replace("could"  , "")
                query = query.replace("can"  , "")
                query = query.replace("you"  , "")
                query = query.replace("please"  , "")
                query = query.replace("browse"  , "")
                query = query.replace("check"  , "")
                query = query.replace("according"  , "")
                query = query.replace("to"  , "")
                query = query.replace("is"  , "")
                query = query.replace("for"  , "")
                
                #Using Wikipedia module to access Wikipedia Info
                try:
                    results = wikipedia.summary(query , auto_suggest=False , sentences = 2)
                    speak("Here is the closest matching result I found for your query ")
                    print (results)
                    speak(results)
                    speak("Do you want me to read more?")
                    newQuery1 = takeCommand().lower()
                    if "yes" in newQuery1:
                        results = wikipedia.summary(query , auto_suggest=False , sentences = 5)
                        print(results)
                        speak(results)
                        webbrowser.register('chrome',None,
                        webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                        webbrowser.get('chrome').open(f"https://en.wikipedia.org/wiki/{query}")
                        speak(f"For more info about {query} , check this out")
                    else:
                        speak("ok")
                except:
                    speak(f"I couldn't find any info about {query}")
                    

               
                        
            elif "open youtube" in query:
                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open("www.youtube.com")
                print("Opening Youtube")
                speak("Opening Youtube")

            elif "open google" in query:
                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open("www.google.in")
                print("Opening Google")
                speak("Opening Google")

            elif "song" in query :
                speak("Which song do you want me to play?")
                song = takeCommand().lower()
                song = song.replace("the song" , "")
                song = song.replace("it" , "")
                song = song.replace("song" ,"")
                song = song.replace("is", "")
                song = song.replace("actually" , "")
                song = song.replace("hey" , "")
                song = song.replace("delta", "")
                song = song.replace("you know" , "")
                song = song.replace("I guess" , "")
                song = song.replace("lookup for" , "")
                song = song.replace("look out for" , "")
                song = song.replace("dear" , "")
                song = song.replace("could you open" , "")
                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open(f"https://open.spotify.com/search/{song}")
                print(f"Searching Spotify for {song}")
                speak(f"Searching Spotify for {song}")

            elif "music playlist" in query:
                
                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open("https://www.youtube.com/playlist?list=PLPpXBmEDOPV4D7IYj3dRn--IAvgwvktlW")
                print("Opening your Bass Music playlist")
                speak("Opening your Bass Music playlist")
                

            elif "open python" in query:
                speak("Do you want me to open official site or documentation")
                newQuery = takeCommand()
                if "official" in newQuery:
                    webbrowser.register('chrome',None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open("www.python.org")
                    print("Opening Python Official Site")
                    speak("Opening Python Official Site")

                elif "docs" or "documentation" in newQuery:
                    webbrowser.register('chrome',None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                    webbrowser.get('chrome').open("docs.python.org/3/")
                    print("Opening Python Documentation of Version 3")
                    speak("Opening Python Documentation of Version 3")
            
            elif "search google" in query:
                query = query.replace("search google" , "")
                query = query.replace("for"  , "")
                query = query.replace("hey"  , "")
                query = query.replace("delta"  , "")
                query = query.replace("could"  , "")
                query = query.replace("can"  , "")
                query = query.replace("please"  , "")
                query = query.replace("you"  , "")

                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open(f"www.google.in/search?q={query}")
                print(f"Searching google for {query}")
                speak(f"Searching google for {query}")
            

            
            elif "search youtube" in query:
                query = query.replace("search youtube" , "")
                query = query.replace("for"  , "")
                query = query.replace("hey"  , "")
                query = query.replace("delta"  , "")
                query = query.replace("could"  , "")
                query = query.replace("can"  , "")
                query = query.replace("please"  , "")
                query = query.replace("you"  , "")
                

                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open(f"www.youtube.in/results?search_query={query}")
                print(f"Searching youtube for {query}")
                speak(f"Searching youtube for {query}")

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is {strTime}")
                speak(f"The time is {strTime}")
            
            elif "joke" in query:
                joke = pyjokes.get_joke()
                speak("Here is a joke for programmers")
                print(joke)
                speak(joke)

            elif "capture" in query or "take photo" in query or "camera" in query:
                speak("capturing a photo through your cam")
                ec.capture(0,"deltaCam" , "img.png")
            
            elif "the weather" in query or "forecast" in query:
                
                speak("Which cities forecast do you want me to look up for?")
                city = takeCommand().lower()
                city = city.replace("the city" , "")
                city = city.replace("it" , "")
                city = city.replace("city" ,"")
                city = city.replace("is", "")
                city = city.replace("actually" , "")
                city = city.replace("hey" , "")
                city = city.replace("delta", "")
                city = city.replace("you know" , "")
                city = city.replace("I guess" , "")
                city = city.replace("lookup for" , "")
                city = city.replace("look out for" , "")
                city = city.replace("dear" , "")
                
                if city != None:
                    if city.lower() == "my location" or  city.lower() == "current location":
                        speak(f"Searching my database for your location's weather forecast details")
                        asyncio.run(getweather(city))
                    else:  
                        speak(f"Searching my database for {city}'s weather forecast details")
                        asyncio.run(getweather(city))
                else:
                    speak("Please specify the city and try again")
            
            elif  "what is" in query or "who is" in query or "where is" in query or "why is" in query or "how is" in query:
                query = query.replace("hey" , "")
                query = query.replace("delta" , "")
                query = query.replace("can you" , "")
                query = query.replace("could you" , "")
                query = query.replace("tell me" , "")
                query = query.replace("say me" , "")
                query = query.replace("search" , "")
                query = query.replace("find me" , "")
                query = query.replace("dear" , "")                
                speak(f"Searching my database for {query}")
                Q = query
                searchDatabase(Q)

            elif "empty recycle bin" in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin emptied")
                speak("Recycle Bin emptied")       

            
            
            elif "calculate" in query:
                speak("please enter what to calculate below")
                Q = input("Question: ")
                speak("Calculating that")
                print("Calculating...")
                searchDatabase(Q)

            elif "mean" in query:
                query = query.replace("hey" , "")
                query = query.replace("delta" , "")
                query = query.replace("can you" , "")
                query = query.replace("could you" , "")
                query = query.replace("tell me" , "")
                query = query.replace("say me" , "")
                query = query.replace("search" , "")
                query = query.replace("find me" , "")
                query = query.replace("dear" , "") 
                query = query.replace("say" , "")
                query = query.replace("what does " , "")
                query = query.replace("meanings" , "") 
                query = query.replace("meaning" , "")  
                query = query.replace("mean" , "")
                
                query = query.replace("of" , "") 

                word = query
                getMeaning(word)
            
            elif "synonym" in query:
                query = query.replace("hey" , "")
                query = query.replace("delta" , "")
                query = query.replace("can you" , "")
                query = query.replace("could you" , "")
                query = query.replace("tell me" , "")
                query = query.replace("say me" , "")
                query = query.replace("search" , "")
                query = query.replace("find me" , "")
                query = query.replace("dear" , "") 
                query = query.replace("say" , "")
                query = query.replace("what does " , "") 
                query = query.replace("synonyms" , "") 
                query = query.replace("synonym" , "")                
                query = query.replace("synonym's" , "") 
                query = query.replace("of" , "") 

                word = query
                getSynonym(word)

            elif "antonym" in query:
                query = query.replace("hey" , "")
                query = query.replace("delta" , "")
                query = query.replace("can you" , "")
                query = query.replace("could you" , "")
                query = query.replace("tell me" , "")
                query = query.replace("say me" , "")
                query = query.replace("search" , "")
                query = query.replace("find me" , "")
                query = query.replace("dear" , "") 
                query = query.replace("say" , "")
                query = query.replace("what does " , "") 
                query = query.replace("antonyms" , "") 
                query = query.replace("antonym" , "")                
                query = query.replace("of" , "") 

                word = query
                getAntonym(word)

            elif "doctor stone soundtrack" in query:
                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open("https://www.youtube.com/playlist?list=PLPpXBmEDOPV4vYuwMJoCnHiOa7fF51e1A")
                speak("Opening Dr.Stone O S T Soundtrack")

            elif "doctor stone" in query:

                webbrowser.register('chrome',None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open("https://flixhd.cc/tv/watch-dr-stone-full-42231")
                speak("Opening Dr.Stone Anime")

            
            elif "open" in query:
                query = query.replace("know"  , "")
                query = query.replace("kind off"  , "")
                query = query.replace("for"  , "")
                query = query.replace("hey"  , "")
                query = query.replace("delta"  , "")
                query = query.replace("could"  , "")
                query = query.replace("can"  , "")
                query = query.replace("you"  , "")
                query = query.replace("please"  , "")                                   
                query = query.replace("me"  , "")
                query = query.replace("now"  , "")
                query = query.replace("open"  , "")
                query = query.replace("start"  , "")
                query = query.replace("run"  , "")

                
                AppOpener.run(query.capitalize())
                speak(f"trying to open {query} application")

            elif "translate" in query:
                speak("Specify which language to translate to")
                to_lang = input("Language: ")
                translate(to_lang)

            elif "download video" in query or "download youtube video" in query:
                speak("Enter your youtube video's URL link")
                url = input("YouTube Video URL:")
                DownloadVideo(url)

            elif "download audio" in query or "extract audio" in query:
                speak("Enter your youtube video's URL link")
                url = input("YouTube Video URL:")
                DownloadAudio(url)

            elif "convert" in query:
                speak("Sure , Please enter the requested data to process your file")
                fromType = input("From File Format(.xxx) --> include (.) : ")
                ToType = input("To File Format(.xxx) --> include (.) : ")
                convertFileType(fromType , ToType)

            elif "capture screen" in query or "screenshot" in query:
                screenShot()
            
            elif "snip" in query:
                snip()

            elif "news" in query or "affair" in query or "what's going on" in query or "what is going on" in query or "whats going on" in query or "update me" in query:
                if "science" in query or "signs" in query or "sites"in query:
                    speak("requesting by database to obtain science news headlines")
                    getScienceNews()
                elif "world" in query:
                    speak("requesting by database to obtain international news headlines")
                    getWorldNews()
                elif "nation" in query:
                    speak("requesting by database to obtain national news headlines")
                    getNationNews()

                elif "business" in query:
                    speak("requesting by database to obtain business news headlines")
                    getBusinessNews()

                elif "tech" in query:
                    speak("requesting by database to obtain tech news headlines")
                    getTechNews()
                elif "entertainment" in query:
                    speak("requesting by database to obtain entertainment news headlines")
                    getEntertainmentNews()

                elif "sports" in query:
                    speak("requesting by database to obtain sports news headlines")
                    getSportsNews()

                elif "health" in query:
                    speak("requesting by database to obtain health news headlines")
                    getHealthNews()
                else:
                    speak("requesting by database to obtain top news headlines")
                    getTopNews()
            
            elif "shutdown" in query or "shut down" in query:
                shutdown()

            elif "sleep" in query or "suspend" in query or "hibernate" in query or "hibernation" in query:
                sleepPC()
            
            elif "logout" in query or "sign out" in query or "log out" in query:
                logout()
            
            elif "restart" in query:
                restart()

            elif "quit" in query or " close " in query or "good bye" in query or "exit" in query:
                speak("terminating project delta ")
                exit()                       

            elif "thanks" in query or "thank you" in query:
                print("You're Welcome!")
                speak("You're Welcome!")

            


    

        


            


    
                

            
        






