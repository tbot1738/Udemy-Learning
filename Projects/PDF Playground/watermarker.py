import PyPDF2 as pp

template = pp.PdfFileReader(open("binded.pdf", "rb"))

watermark = pp.PdfFileReader(open("wtr.pdf", "rb"))

output = pp.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked.pdf","wb") as file:
        output.write(file)
        