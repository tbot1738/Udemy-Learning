import PyPDF2 as pp
import sys

inputs = sys.argv[1:]

def pdf_rotater():
    with open("dummy.pdf", "rb") as file:
        reader = pp.PdfFileReader(file)
        page = reader.getPage(0)
        rotate = page.rotateClockwise(90)
        writer = pp.PdfFileWriter()
        writer.addPage(page)
        with open("tilted.pdf", "wb") as new_file:
            writer.write(new_file)

def merge(pdf_lists):
    merger = pp.PdfFileMerger()
    for pdf in pdf_lists:
        print(pdf)
        merger.append(pdf)
    merger.write("Binded.pdf")
merge(inputs)
