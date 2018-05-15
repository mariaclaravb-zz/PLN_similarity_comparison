# -*- coding: utf-8 -*-

import PyPDF2
import os


def pdf_to_text(file_path):
    pdf_reader = PyPDF2.PdfFileReader(file_path)
    text = ''
    for page in pdf_reader.pages:
        text += page.extractText()
    return text


def merge_from_path(path):
    with open("{}.txt".format(path[:-8]), 'w') as file:
        for temp in os.listdir(path):
            if temp.endswith('.txt'):
                file_path = path + temp
                with open(file_path, "r") as t:
                    file.writelines(t)


if __name__ == '__main__':

    # paths = ["feminismo/", "liberalismo/", "marxismo/"]
    paths = ["liberalismo/"]

    # Convert pdf to text
    for path in paths:
        path += 'pdfs/'
        for file_name in os.listdir(path):
            file_path = path + file_name
            file = open(file_path.replace('.pdf', '.txt').replace('pdfs/', 'textos/'), 'w')
            file.write(pdf_to_text(file_path))
            file.close()

    for path in paths:
        merge_from_path(path + 'textos/')
