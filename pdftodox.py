from pdf2docx import Converter
int_file = input("lütfen dosya adını giriniz: ")
yeni_doc = "out.doc"
file = Converter(int_file)
file.convert(yeni_doc)
file.close()