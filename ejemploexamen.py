n_e = str(input("Escriba Nombre completo del estudiante ")).capitalize()
not_e = float(input("Escriba nota del estudiante "))
if not_e > 90 and not_e <=100:
    print((n_e), "tiene un rendimiento : Excelente")
if not_e > 70 and not_e <=90:
    print((n_e), "tiene un rendimiento : Bueno")    
if not_e > 50 and not_e <=70:
    print((n_e), "tiene un rendimiento : Regular")  
if not_e >= 0 and not_e <=50:
    print((n_e), "tiene un rendimiento : Insuficiente")      
    