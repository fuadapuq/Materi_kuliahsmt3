# membuat class
class Mobil:
    #membuat class variable
    jumlah_mobil = 0 

    def __init__(self, ban, merk, cc):
        self.merkban = ban
        self.merkmobil = merk
        self.kapasitas = cc
        Mobil.jumlah_mobil += 1
        
 #membuat method string       
    def __str__(self):
        return f"{self.merkban}, {self.merkmobil}, {self.kapasitas}"
    
    # membuat method baru menambah Boreup
    def borup(self, bore):
        self.kapasitas += bore

# membuat Objek Baru M1
M1 = Mobil("Bridgestone", "Toyota-Kijang", 1500)
print(M1)
print("Jumlah mobil:", Mobil.jumlah_mobil)
M1.boreup(500)
print(M1)

# membuat Objek Baru M2
M2 = Mobil("Pirelli", "Subaru", 1000)
print(M2)
print("Jumlah mobil:", Mobil.jumlah_mobil)
M2.boreup(500)
print(M2)

