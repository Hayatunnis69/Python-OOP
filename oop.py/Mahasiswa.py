#memebuat class dengan kata kunci "class"

class Mahasiswa:
    #atribute
    #konstruktor
    def __init__(self, nim, nama, rombel) :
        #variabel objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
        
    #methode
    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
    #class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Rombel :", self.rombel)
        #print("keterangan :", self.lulus)

#membuat objek
mahasiswa1 = Mahasiswa("0110222", "Atun", "TI 05")
#mencetak atribut
mahasiswa1.cetak()
mahasiswa1.lulus(95)

#ojek ke 2
mahasiswa2 = Mahasiswa("0221189", "Nisa", "SI 12") 
#mencetak atribut
mahasiswa2.cetak()
mahasiswa2.lulus(85)


#print(help(Mahasiswa1.nama))
