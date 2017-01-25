import PyPDF2
import re
#import docx


def text_compiler(pdf, pages):
    page_count = 0

    while page_count < pages:
        text.append(pdf.getPage(page_count))
        page_count += 1

    for page in text:
        extracted_text.append(page.extractText())


def pdf_file_info():
    pdf_file_object = open('/Users/michaelporter/Desktop/Personal/UTPB/ENGL 2327/Paper1.pdf', 'rb')

    pdf_document_data = PyPDF2.PdfFileReader(pdf_file_object)

    return pdf_document_data


def page_count(doc):
    how_many_pages = doc.getNumPages()
    # print(how_many_pages)

    return how_many_pages


def combine_string():
    string_combined = ''
    for page in extracted_text:
        string_combined = page + string_combined

    # print(string_combined)
    return string_combined


def main():
    text_compiler(pdf_file_info(), page_count(pdf_file_info()))
    #combine_string()


text = []
extracted_text = []

main()

for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)', extracted_text[0]):
    print(match.start(), match.end())
