"""
Project Title : AI Based Software tool for Blind People
"""
import pyttsx3
import speech_recognition as sr
import PyPDF2
from PyDictionary import PyDictionary
import Book_List
recognizer = sr.Recognizer()

speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
# print(voices[2].id)
speaker.setProperty("voice", voices[0].id)
# Voice name: Microsoft Heera - English (India)
speaker.setProperty("rate", 145)
with sr.Microphone() as source:
    speaker.say("""Hello,
    I'm your Software tool for e-Learning
    I can read pdf text file and refer dictionary""")
    speaker.runAndWait()
    speaker.say("Do you want me to read pdf or search in dictionary")
    speaker.runAndWait()
    speaker.say("""if you want to me to read a file say 'read'
    Else say any word like 'word' """)
    speaker.runAndWait()
    print("Clearing background noise..")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Waiting for your choice...")
    recorded_audio1 = recognizer.listen(source)
    print("Done recording...")
    print("Printing your choice: ", end=" ")
    try:
        recognizer.recognize_google(recorded_audio1, language="en-IN")
    except sr.UnknownValueError:
        speaker.say("Sorry! speak clearly ")
        speaker.runAndWait()
        exit(0)
    choice = recognizer.recognize_google(recorded_audio1, language="en-IN")
    print(choice)
    if choice.lower() == "read":
        with sr.Microphone() as source:
            speaker.say("Tell me book name")
            speaker.runAndWait()
            print("Clearing background noise..")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Waiting for book name ...")
            recorded_audio2 = recognizer.listen(source)
            print("Done recording...")
            print("Printing book name: ", end=" ")
        try:
            recognizer.recognize_google(recorded_audio2, language="en-IN")
        except sr.UnknownValueError:
            speaker.say("Sorry! speak clearly ")
            speaker.runAndWait()
            exit(0)
        name = recognizer.recognize_google(recorded_audio2, language="en-IN")
        print(name)
        try:
            (Book_List.book_name(name.lower()))
        except NameError or KeyError:
            speaker.say("""Unable to find Book.
            Try after updating your Book List """)
            speaker.runAndWait()
            exit(0)
        book_name = str(Book_List.book_name(name.lower()))
        print(book_name)

        book = open(book_name, "rb")
        pdfReader = PyPDF2.PdfReader(book)
        pages = len(pdfReader.pages)
        print("Number of pages in book:", pages)
        for num in range(pages):
            page = pdfReader.pages[num]
            text = page.extract_text()
            speaker.say(text)
            speaker.runAndWait()
            speaker.say("Completed Reading your book")
            speaker.runAndWait()
    else:
        with sr.Microphone() as source:
            speaker.say("Tell me word to search")
            speaker.runAndWait()
            print("Clearing background noise..")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Waiting for word ...")
            recorded_audio3 = recognizer.listen(source)
            print("Done recording...")
            print("Printing word: ", end=" ")
        try:
            recognizer.recognize_google(recorded_audio3, language="en-IN")
        except sr.UnknownValueError:
            speaker.say("Sorry! speak clearly ")
            speaker.runAndWait()
            exit(0)
        word = recognizer.recognize_google(recorded_audio3, language="en-IN")
        print(word)
        dictionary = PyDictionary(word)
        speaker.say("All details about suggested word:")
        speaker.runAndWait()
        speaker.say("Meaning")
        speaker.runAndWait()
        speaker.say(dictionary.meaning(word))
        speaker.runAndWait()
        speaker.say("Synonyms")
        speaker.runAndWait()
        speaker.say(dictionary.getSynonyms(word))
        speaker.runAndWait()
        speaker.say("Antonyms")
        speaker.runAndWait()
        speaker.say(dictionary.getAntonyms(word))
        speaker.runAndWait()
        speaker.say("Reading Information is completed")
        speaker.runAndWait()