#! python3

import  docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append('\t' + para.text)
    return '\n\n'.join(fullText)


print(getText('demo.docx'))
