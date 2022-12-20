import PyPDF3, pyttsx3, pdfplumber

file = open('FILE_NAME', 'rb')
pdfReader = PyPDF3.PdfFileReader(file)
num_pages = pdfReader.numPages
clean_text = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, num_pages):
        page = pdf.pages[i]
        text = page.extract_text()
        clean_text += text
print(clean_text)


converter = pyttsx3.init()
#converter.say(clean_text)
converter.save_to_file(clean_text, 'test.mp3')
converter.runAndWait()
