import speech_recognition as sr
import pyttsx3
import playsound
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import yfinance as yf



listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("I am Alexa, what I can do for you")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('listening...')
            command = input("Enter command: ")
            # voice = listener.listen(source)
            # command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa, ', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    # 4: time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'price of' in command:
        search_term = command.replace('price of ', '')
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD",
            "ethereum": "ETH-USD"
        }
        stock = stocks[search_term]
        stock = yf.Ticker(stock)
        price = stock.info["regularMarketPrice"]
        talk(f'price of {search_term} is {price} {stock.info["currency"]} ')
    elif "search for" in command:
        search_term = command.replace("search for ", '')
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        talk(f'Here is what I found for {search_term} on google')
    elif "weather" in command:
        search_term = command.replace("weather", '')
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        talk("Here is what I found for on google")
    # elif "plus" or "minus" or "multiply" or "divide" or "power" or "+" or "-" or "*" or "/" in command:
    #     opr = command.split()[1]
    #
    #     if opr == '+':
    #         talk(int(command.split()[0]) + int(command.split()[2]))
    #     elif opr == '-' or 'minus':
    #         talk(int(command.split()[0]) - int(command.split()[2]))
    #     elif opr == 'multiply' or '*':
    #         talk(int(command.split()[0]) * int(command.split()[2]))
    #     elif opr == 'divide' or '/':
    #         talk(int(command.split()[0]) / int(command.split()[2]))
    #     elif opr == 'power':
    #         talk(int(command.split()[0]) ** int(command.split()[2]))
    #     else:
    #         talk("Wrong Operator")
    # elif "how are you" or "how are you doing" in command:
    #     talk("I'm very well, thanks for asking ")
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "goodbye" in command:
        talk("going offline")
        exit()
    elif "where is" in command:
        query = command.replace(" where is", '')
        location = query
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.com / maps / place/" + location + "")

    else:
        talk('Please say the command again.')


while True:
    run_alexa()
