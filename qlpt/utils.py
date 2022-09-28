import os
# import docx

from PC07.settings import BASE_DIR


# def doc_replace(doc, findText, replaceText):
#     for p in doc.paragraphs:
#         if findText in p.text:
#             inline = p.runs
#             for i in range(len(inline)):
#                 if findText in inline[i].text:
#                     text = inline[i].text.replace(
#                         findText, replaceText)
#                     inline[i].text = text


def text_to_mp3(text):
    import pyttsx3
    bot = pyttsx3.init()
    bot.setProperty('rate', 125)
    bot.setProperty('volume', 1.0)
    voices = bot.getProperty('voices')
    bot.setProperty('voice', voices[4].id)
    import time
    ts = time.time()
    filename = os.path.join(BASE_DIR, "static/mp3")+'/'+str(ts)+'.mp3'
    bot.save_to_file(text, filename)
    bot.runAndWait()
    return filename


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
    bot.save_to_file(text, 'E:/test.mp3')
    bot.runAndWait()


# doc = docx.Document("C:/Users/ADMIN/Desktop/cv.docx")
# for p in doc.paragraphs:
#     speak(p.text)
# speak('Sơ vơ đã bật')
