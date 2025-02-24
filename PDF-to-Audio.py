from gtts import gTTS
import os
from pypdf import PdfReader
#Path of the PDF File
FilePath = ''

#Specify the language of the Audio
Language = ''

#The Audio Filename (The extension must be an Audio file)
OutputName = ''

File = PdfReader(FilePath)
Content = ""
for i in range(len(File.pages)):
    #Reading the entire PDF
    Content += File.pages[i].extract_text()


Audio = gTTS(text=Content, lang=Language , slow=False)
Audio.save(OutputName)

