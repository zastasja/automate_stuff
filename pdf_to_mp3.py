import pdfplumber, pyttsx3

## works with English text only

with pdfplumber.PDF(open(file=f'task_a.pdf', mode='rb')) as pdf:
    pages = [page.extract_text() for page in pdf.pages]

text = ''.join(pages)
text = text.replace('\n', '')

speaker = pyttsx3.init()
speaker.save_to_file(text, 'task_a.mp3')
speaker.runAndWait()
speaker.stop()