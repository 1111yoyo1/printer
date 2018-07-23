import win32print
import win32api

#source_file_name = "d:/1.txt"
#source_file_name = "d:/UNH-IOL_NVMe_Interop_Test_Suite_v9.0.pdf"
#pdf_file_name = tempfile.mktemp(".pdf")

currentprinter = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, "print", 'test.pdf', '/d:"%s"' % currentprinter, ".", 0)
