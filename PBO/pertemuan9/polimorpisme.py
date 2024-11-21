#tanpa implementasi polimormisme
class Jumlah:
    def tambah1(n1,n2):
        print(f"Hasilnya {n1+n2}")
objek3= Jumlah
objek3.tambah1(1,2)
#implementasi polimorfisme
class Penjumlahan:
    def tambah(*num):
            return sum(num)
objek1= Penjumlahan
print(objek1.tambah(2,3))

#menggunakan default parameter
class default:
    def tambah2(self,a, b,c=0,d=0,e=0):
        print (f"Hasilnya {a+b+c+d+e}")
objek2 = default
objek2.tambah2(2,4,2,3,5)