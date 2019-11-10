##Program Akun
##Dibuat oleh Clara Sekar D.H L200190207
import random
angka = random.randint(0,1000)

Nama = 'Clara Sekar Desanti Haryono'
TanggalLahir = '25 Desember 2000'
NamaSingkat = Nama[0] + '.' + Nama[6] + '.' + Nama[12] + '.' + Nama[20:27]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir [12:16]
Password = Nama [0:4] + str(angka)

print (Nama)
print (TanggalLahir)
print (NamaSingkat)
print (Username)
print (Password)
