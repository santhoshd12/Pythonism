import pyttsx3 
import PyPDF2
engine = pyttsx3.init()
engine.setProperty('rate',150)
pdf = open('unit.pdf','rb')
pdfread = PyPDF2.PdfReader(pdf) 
print(len(pdfread.pages))
  
# for i in range(2,4):
#     page = pdfread.pages[i]
#     text = page.extract_text()
#     engine.say(text)

page = pdfread.pages[0]
text = page.extract_text()
op = "texttospeech.mp3"
#engine.say(text)
engine.save_to_file(text,op)

engine.runAndWait()
