import pypandoc

def convert_docx_to_pdf(docx_path, pdf_path):
    pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)

convert_docx_to_pdf("TA3.docx", "TA3.pdf")





