peso= 0
alt= 0
imc= peso / alt ^ 2
if imc < 20:
    print (imc)
    print ("Usted está bajo de peso")
if imc >= 20 and imc  <= 24.99:
    print (imc)
    print ("Usted está en peso normal")   
if imc >= 25 and imc  <= 29.99:
    print (imc)
    print ("Usted tiene obesidad leve")   
if imc >= 30 and imc  <= 39.99:
    print (imc)
    print ("Usted tiene obesidad severa")       
if imc >40:
    print (imc)
    print ("Usted tiene obesidad muy severa")       