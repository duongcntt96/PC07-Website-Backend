def speak(text):
    import pyttsx3
    bot = pyttsx3.init()
    bot.setProperty('rate', 125)
    bot.setProperty('volume', 1.0)
    voices = bot.getProperty('voices')
    bot.setProperty('voice', voices[4].id)
    print(voices)
    for voice in voices:
        print(voice)
    bot.say(text)
    # bot.save_to_file(text, 'E:/test.mp3')
    bot.runAndWait()


speak('Bây giờ là 1 giờ 42 phút')
