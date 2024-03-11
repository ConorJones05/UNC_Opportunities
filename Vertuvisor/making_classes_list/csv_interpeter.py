import PyPDF2
PDF = "ConorJonesProjects/Vertuvisor/making_classes_list/2242-SSB-10-9-23.pdf"


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Example usage:
pdf_path = PDF
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)