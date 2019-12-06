import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "program komunikasi tentang data diri"
data = ""
kamus = {"nama":"Clara Sekar D H",
         "NIM":"L200190207",
         "angkatan":"2019",
         "keluar":"Siap!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower()!= "keluar":
        data = komm.recv(1025)
        print "perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("maaf, perintah tidak dimengerti")
