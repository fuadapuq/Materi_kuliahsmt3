# Membuat sebuah Super Class
class Animal:
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras
    
    #membuat method bersuara
    def Speaks(self):
        print(f"{self.name} bisa bersuara")
# Membuat kelas turunan dari super kelas
class Cat(Animal):
    def Sounds(self):
        print(f"Nama{self.name} dengan Ras {self.ras} bersuara Meooowwww")
#membuat kelas 2 turunan dari super kelas
class Dog(Animal):
    def speaksDog(self):
        print(f"Nama{self.name} dari Ras {self.ras} Bersuara Guk Guk")
#membuat Objek
cat = Cat("Kitty", "Angora")
cat.speaksCat()