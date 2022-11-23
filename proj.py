from ast import main
from multiprocessing.spawn import _main
import pyttsx3;
import datetime;
# import pyaudio;
import speech_recognition as sr;
import wikipedia
import webbrowser;
import os;


Engines=pyttsx3.init('sapi5')
#The sapi5 is used to the inbuilt voice provide by the microsoft windows.
voice=Engines.getProperty('voices');

"""print(voice[0].id); The voice return two thing in pytssx3 it means i can add the voices or the voice is one is male and another one is female.i have to chose any one.
print(voice[1].id);This is an women voice to select [voice[1].id]"""
Engines.setProperty('voice',voice[0].id);

def speak(audio):
    Engines.say(audio);
    Engines.runAndWait();

#wishing a morning and afternoon schedule according to time.
def wishMe():
    hour=int(datetime.datetime.now().hour);
    if(hour>=0 and hour<12):
        speak("Good Morning");
    elif(hour>=12 and hour<18):
        speak("Good Afternoon");
    else:
        speak("Good Evening");

    speak("how can i help you");

#it used to user give the voice.
def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r=sr.Recognizer();#To recongnize the audio
    with sr.Microphone() as source:
        print("Listening..");
        r.pause_threshold=1;
        audio=r.listen(source);
    try:
        print("Recognizing...");
        query=r.recognize_google(audio,language='en-us');
        print("user said:-",query);
    except Exception as e:
        print("Say that Again");
        return "None";
    return query;



    
if __name__ == "__main__":
    wishMe();
    #akeCommand();
    query=takeCommand().lower();
    if 'wikipedia' in query:
        speak("searching wikepidia");
        query=query.replace("wikipedia","");
        results=wikipedia.summary(query, sentences=2);
        speak("According to wikipedia");
        #print(results);
        speak(results);

    elif 'open youtube' in  query:
        webbrowser.open("youtube.com");

    elif 'open google' in  query:
        webbrowser.open("google.com");
        
    elif 'open stack overflow' in  query:
        webbrowser.open("stackoverflow.com");

    elif 'tell time' in query:
        strTimes=datetime.datetime.now().strftime("%H:%M:%S");
        speak(f"sir the time is {strTimes}");
        print(strTimes) 


    elif "open code" in query:
        path="C:\\Users\\deora\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path);

    


            
