dia = (input())
mes = (input())

def signo_zodiacal(dia, mes):
    if mes == "1":
        if dia < "21":
            print("eres capricornio")
        else:
            print("eres acuario")
    elif mes == "2":
        if dia < "20":
            print("eres acuario")
        else:
            print("eres piscis")
    elif mes == "3":
        if dia < "21":
            print("eres piscis")
        else:
            print("eres aries")
    elif mes == "4":
        if dia < "20":
            print("eres aries")
        else:
            print("eres tauro")    
    elif mes == "5":
        if dia < "21":
            print("eres tauro")
        else:
            print("eres géminis")
    elif mes == "6":
        if dia < "22":
            print("eres géminis")
        else:
            print("eres cáncer")
    elif mes == "7":
        if dia < "24":
            print("eres cáncer")
        else:
            print("eres leo")
    elif mes == "8":
        if dia < "24":
            print("eres leo")
        else:
            print("eres virgo")
    elif mes == "9":
        if dia < "23":
            print("eres virgo")
        else:
            print("Eres Libra")
    elif mes == "10":
        if dia < "23":
            print("eres libra")
        else:
            print("eres escorpión")
    elif mes == "11":
        if dia < "23":
            print("eres escorpión")
        else:
            print("eres sagitario")
    elif mes == "12":
        if dia < "23":
            print("eres sagitario")
        else:
            print("eres acuario")
    else:
        print("mes no valido")

signo_zodiacal(dia,mes)