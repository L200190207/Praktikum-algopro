Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Clara Sekar Desanti Haryono"
>>> NIM = "L200190207"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len (Nama)
>>> type (a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi type data integer
>>> type (b)
<class 'int'>
>>> #Karena data "Nama" memiliki intruksi "len"
>>> a / b
44.7037037037037
>>> #Karena "/" pembagian, maka 1207 dibagi 27 adalah 44.7037037037037
>>> a // b
44
>>> #karena // merupakan pembagian yang dibulatkan ke bawah
>>> 10 * (a - 999)
2080
>>> #karena nilai "a" dikurangi 999 adalah 208, kemudian dikalikan 10 adalah 2080
>>> b ** 2
729
>>> #karena pengertian dari "**" adalah perpangkatan, maka nilai "b" dipangkatkan "2" adalah 729
>>> a % b
19
>>> #karena arti dari "%" adalah sisa hasil bagi , maka nilai sisa hasil baginya adalah 19
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #Karena 12.5 adalah bilangan desimal sehingga termasuk kedalam type data float
>>> a / c
96.56
>>> #Karena arti dari 1207 dibagi 12.5 adalah 96.56
>>> a // c
96.0
>>> #Karena arti dari "//" adalah pembagian dibulatkan kebawah jadi hasilnya 96.0
>>> a % c
7.0
>>> #Karena arti dari % adalah sisa bagi, dan sisa dari 1207 dibagi dengan 12.5 adalah 7.0
>>> c > b
False
>>> #Karena nilai "c" lebih besar dari "b" adalah salah
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki kedua kemungkinan yaitu True atau False
>>> a > b and b > c
True
>>> #Karena logika "DAN" True and True menghasilkan nilai True
>>> a > 1100 or b < 10
True
>>> #Karena logika "ATAU" True or False menghasilkan nilai True
>>> 
