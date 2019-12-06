import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server siap"
perintah=''
pi=0
r=0
t=0
while perintah !='keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item)==2:
            if perintah == 'pi':
                pi=float(item[1])
                komm.send('pi disimpan')
            elif perintah == 'jari-jari':
                r=int(item[1])
                komm.send('jari-jari disimpan')
            elif perintah == 'tinggi':
                t=int(item[1])
                komm.send('tinggi disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(2*pi*r*(r+t))
            response = 'Luas tabung dengan pi (3.14) jari-jari {} tinggi {} adalah {}'.format(r,t,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
