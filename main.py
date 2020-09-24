dia = (input())
mes = (input())
signo = " "

if mes == "1":
    if dia < "21":
        signo = "eres capricornio"
    else:
        signo = "eres acuario"
elif mes == "2":
    if dia < "20":
        signo = "eres acuario"
    else:
        signo = "eres piscis"
elif mes == "3":
    if dia < "21":
        signo = "eres piscis"
    else:
        signo = "eres aries"
elif mes == "4":
    if dia < "20":
        signo = "eres aries"
    else:
        signo = "eres tauro"  
elif mes == "5":
    if dia < "21":
        signo = "eres tauro"
    else:
        signo = "eres géminis"
elif mes == "6":
    if dia < "22":
        signo = "eres géminis"
    else:
        signo = "eres cáncer"
elif mes == "7":
    if dia < "24":
        signo = "eres cáncer"
    else:
        signo = "eres leo"
elif mes == "8":
    if dia < "24":
        signo = "eres leo"
    else:
        signo = "eres virgo"
elif mes == "9":
    if dia < "23":
        signo = "eres virgo"
    else:
        signo = "Eres Libra"
elif mes == "10":
    if dia < "23":
        signo ="eres libra"
    else:
        signo = "eres escorpión"
elif mes == "11":
    if dia < "23":
        signo = "eres escorpión"
    else:
        signo = "eres sagitario"
elif mes == "12":
    if dia < "23":
        signo = "eres sagitario"
    else:
        signo = "eres acuario"
else:
    signo = "mes no valido"   

print (signo)