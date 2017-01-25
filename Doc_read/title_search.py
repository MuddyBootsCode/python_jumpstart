import PyPDF2
import re


def text_compiler(pdf, pages):
    page_count = 0

    while page_count < pages:
        text.append(pdf.getPage(page_count))
        page_count += 1

    for page in text:
        extracted_text.append(page.extractText())


# def print_text():
#     for page in extracted_text:
#         print(page)


def combine_string():
    string_combined = ''
    for page in extracted_text:
        string_combined = page + string_combined

    print(len(string_combined))
    return string_combined


def pdf_file_info():
    pdf_file_object = open('/Users/michaelporter/Desktop/joa.pdf', 'rb')

    pdf_document_data = PyPDF2.PdfFileReader(pdf_file_object)

    return pdf_document_data


def page_count(doc):
    how_many_pages = doc.getNumPages()
    print(how_many_pages)

    return how_many_pages


def finder():
    user_search = input('What is your search query?')
    user_search = user_search.strip()

    if user_search.lower() in combine_string().lower():
        print('Found it!')
    else:
        print('Not here!')


def main():
    text_compiler(pdf_file_info(), page_count(pdf_file_info()))
    # print_text()
    combine_string()
    finder()



text = []
extracted_text = []

main()
