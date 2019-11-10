Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Clara Sekar Desanti Haryono"
>>> NIM = 207
>>> Tinggi = 1.64
>>> Berat = 49
>>> TahunLahir= 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> type(Aku)
<class 'tuple'>
>>>  #Karena data "Aku" ditulis dengan menggunakan tanda kurung biasa dan item di dalamnya tidak dapat diubah
>>> Aku[0]
2000
>>> #Karena item pertama dari data "Aku" adalah "TahunLahir", dan nilai dari "TahunLahir"
>>> a = NIM % 4; Aku[a]
207
>>>  #Karena sisa hasil bagi dari 207 dibagi 4 adalah 3, jadi hasil dari Aku[0] adalah 2000
>>> type (Aku[a])
<class 'int'>
>>> #Karena Aku[0] adalah "TahunLahir" dan nilainya 2000, 2000 adalah tipe data integer
>>> Aku[a:4]
(207,)
>>>  #karena a adalah 3 maka data "Aku" adalah "NIM"
>>> type(aku[4])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type(aku[4])
NameError: name 'aku' is not defined
>>> type(Aku[4])
<class 'str'>
>>> #Karena item kelima dari data "Aku" adalah "Nama", dan nilai dari "Nama" adalah "Clara Sekar Desanti Haryono" yang termasuk kedalam tipe data string
>>> Aku[0]= "ok"
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Aku[0]= "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Karena isi tuple tidak dapat diubah (immutable) sehingga terjadi error
>>> type(Data)
<class 'tuple'>
>>>  #Karena data "Data" ditulis dengan menggunakan kurung siku dan koleksi item di dalamnya dapat berubah, bertambah, dan berkurang secara dinamis
>>> type(Data[4])
<class 'str'>
>>> #Karena item kelima dari data "Data" adalah "Nama", dan nilai dari "Nama" adalah "Clara Sekar Desanti Haryono"
>>> Data [4] [5]
' '
>>> #Karena Data[4] atau objek kelima dari "Data" adalah "Nama" dan indeks 5 dari "Nama" adalah " "
>>> Data [4] [a:6]
'ra '
>>> #Karena Data[4] adalah "Nama" dan Nama[3:6] adalah objek pertama sampai objek keenam dari data "Nama" yaitu "ra"
>>> Data [0] = "ok"; Data
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Data [0] = "ok"; Data
TypeError: 'tuple' object does not support item assignment
>>> Data[-a]
1.64
>>> #Karena a adalah 0, jadi indeks 0 dari "Data" adalah objek pertama yaitu "1.64"
>>> range(a)
range(0, 3)
>>> #Karena a adalah 0, jadi range(0) menghasilkan range 0 sampai 3
