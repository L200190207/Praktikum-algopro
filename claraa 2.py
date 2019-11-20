def konverensiSuhu(c=0, f=0):
    if f != 0:
        c =((f-32)*5)//9
        print("Suhu",f,"Fahrenheit setara dengan",c,"Celcius")
    else:
        f=((c*9)//5)+32
        print("Suhu",c,"celcius setara dengan",f,"Fahrenheit")
       
