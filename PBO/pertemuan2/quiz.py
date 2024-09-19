class buku:

    def __init__(self, judul, penulis, tahun_terbit):
        self.namajudul = judul
        self.namapenulis = penulis
        self.tahun_terbit = tahun_terbit
        
       
    def __str__(self):
        return f"{self.namajudul}, {self.namapenulis}, {self.tahun_terbit}"
    
   
    def borup(self, tahun):
        self.tahun_terbit = tahun


A1 = buku("The Lord of the Rings", "J.R.R. Tolkien", 1945)
print(A1)
A1.borup(1950)
print(A1)


A2 = buku("Harry Potter and the Chamber of Secrets", "J. K. Rowling", 1998)
print(A2)
A2.borup(1999)
print(A2)