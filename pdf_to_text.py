import pdfplumber

with pdfplumber.PDF(open(file=f'task_a.pdf', mode='rb')) as pdf:
    pages = [page.extract_text() for page in pdf.pages]

text = ''.join(pages)
text = text.replace('\n', '')
print(text)
