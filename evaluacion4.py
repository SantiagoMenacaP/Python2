n1= 0
n2= 0
n3= 2.5
n4= 5
n_d= n1 * 0.1 + n2 * 0.1 + n3 * 0.4 + n4 * 0.4
if n_d >= 3:
    print ("Su nota fue ", n_d )
    print ("Ganó, felicitaciones")
if n_d < 3 and n_d  >= 2.5:
    print ("Su nota fue ", n_d )
    print ("Perdió, puede habilitar")   
if n_d < 2.5:  
    print ("Su nota fue ", n_d )
    print ("Perdió, debe repetir")  