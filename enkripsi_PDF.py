from PyPDF2 import PdfFileWriter, PdfFileReader
  
# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf asli 
file = PdfFileReader("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/file_pdf.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num):
    
   
    page = file.getPage(idx)
      

    out.addPage(page)
  
  
# masukkan password enkripsi 
password = "pass"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/myfile_encrypted.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)
