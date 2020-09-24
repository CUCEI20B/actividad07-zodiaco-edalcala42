dia = (input())
mes = (input())
signo = " "

if (mes == "1" and dia > "20") or (mes == "2"and dia < "21"):
    signo = "acuario"
elif(mes == "2" and dia > "20") or (mes == "3" and dia < "21"):
    signo = "piscis"
elif(mes == "3" and dia > "20") or (mes == "4" and dia < "21"):
    signo = "aries"
elif(mes == "4" and dia > "20") or (mes == "5" and dia < "21"):
    signo = "tauro"  
elif(mes == "5" and dia > "20") or (mes == "6" and dia < "21"):
    signo = "geminis"
elif(mes == "6" and dia > "20") or (mes == "7" and dia < "21"):
    signo = "cancer"
elif(mes == "7" and dia > "20") or (mes == "8" and dia < "21"):
    signo = "leo"
elif(mes == "8" and dia > "20") or (mes == "9" and dia < "21"):
    signo = "virgo"
elif(mes == "9" and dia > "20") or (mes == "10" and dia < "21"):
    signo = "libra"
elif(mes == "10" and dia > "20") or (mes == "11" and dia < "21"):
    signo = "escorpio"
elif(mes == "11" and dia > "20") or (mes == "12" and dia < "21"):
    signo = "sagitario"
elif(mes == "12" and dia > "20") or (mes == "1" and dia < "21"):
    signo = "capricornio"
print(signo)