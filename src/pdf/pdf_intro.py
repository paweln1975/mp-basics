"""
PDF library training
>>> import sys; sys.tracebacklimit = 0
>>> n, meta = pdf_get_number_of_pages('dummy.pdf')
>>> n == 1
True
>>> create_pdf('write.pdf')
"""

from PyPDF4 import PdfFileReader, PdfFileWriter
from fpdf import FPDF

def pdf_get_number_of_pages(filename) -> tuple[int, str]:
    with open(filename, 'rb') as pdf_file:
        pdf = PdfFileReader(pdf_file)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        if number_of_pages == 1:
            page_0 = pdf.getPage(0)

        metadata = f"""
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
        pdf
        return number_of_pages, metadata


def create_pdf(filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(text="hello world")
    pdf.output(filename)

