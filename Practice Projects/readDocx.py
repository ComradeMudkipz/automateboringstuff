#! /usr/bin/python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)      # use ' ' + para.text to indent.
    return '\n'.join(fullText)          # add another \n to double space
                                        # in between paragraphs.
