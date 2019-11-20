Data = {"NIM" : "L200190207",
        "Nama" : "Clara Sekar D H ",
        "Alamat" : "Perumahan Pakis Pertiwi",
        "TTL" : "Klaten, 25 Desember 2000",
        "Kampus" : "UMS",
        "Fakultas" : "FKI",
        "Jurusan" : "Informatika"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilAlamat():
    print(Data["Alamat"])
def TampilTTL():
    print(Data["TTL"])
def TampilKampus():
    print(Data["Kampus"])
def TampilFakultas():
    print(Data["Fakultas"])
def TampilJurusan():
    print(Data["Jurusan"])

TampilNIM()
TampilNama()
TampilAlamat()
TampilTTL()
TampilKampus()
TampilFakultas()
TampilJurusan()

def x():
    print("Pilihan yang tersedia :")
    print("b menampilkan bantuan ini")
    print("c menampilkan NIM")
    print("d menampilkan Nama")
    print("e menampilkan Alamat")
    print("f menampilkan TTL")
    print("g menampilkan Kampus")
    print("h menampilkan Fakultas")
    print("i menampilkan Jurusan")
    print("k keluar")
def k():
    print("Terima Kasih")
x() 

a= input("Pilihan saudara :")
while a!="k" :
    if a=="b":
        x()
        print("")
        a = input("Pilihan saudara")
    elif a=="c":
        TampilNIM()
        a = input("Pilihan saudara")
    elif a== "d":
        TampilNama()
        a = input("Pilihan saudara")
    elif a== "e":
        TampilAlamat()
        a = input("Pilihan saudara")
    elif a== "f":
        TampilTTL()
        a = input("Pilihan saudara")
    elif a == "g":
        TampilKampus()
        a = input("Pilihan saudara")
    elif a=="h":
        TampilFakultas()
        a = input("Pilihan saudara")
    elif a== "i":
        TampilJurusan()
        a = input("Pilihan saudara")
k()
    
