dia = (input())
mes = (input())

if mes == "1":
    if dia < "21":
        print("capricornio")
    else:
        print("acuario")
elif mes == "2":
    if dia < "20":
        print("acuario")
    else:
        print("piscis")
elif mes == "3":
    if dia < "21":
        print("piscis")
    else:
        print("aries")
elif mes == "4":
    if dia < "20":
        print("aries")
    else:
        print("tauro")    
elif mes == "5":
    if dia < "21":
        print("tauro")
    else:
        print("géminis")
elif mes == "6":
    if dia < "22":
        print("géminis")
    else:
        print("cáncer")
elif mes == "7":
    if dia < "24":
        print("cáncer")
    else:
        print("leo")
elif mes == "8":
    if dia < "24":
        print("leo")
    else:
        print("virgo")
elif mes == "9":
    if dia < "23":
        print("virgo")
    else:
        print("Libra")
elif mes == "10":
    if dia < "23":
        print("libra")
    else:
        print("escorpión")
elif mes == "11":
    if dia < "23":
        print("escorpión")
    else:
        print("sagitario")
elif mes == "12":
    if dia < "23":
        print("sagitario")
    else:
        print("acuario")
else:
    print("mes no valido")    
