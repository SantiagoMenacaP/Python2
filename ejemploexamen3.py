col = input("ingrese el color ").upper()
match col:
    case "ROJO":
        print("enemigo detectado")
    case "VERDE":
        print("camino despejado")
    case "AZUL":
        print("recuperando energia")   
    case _:
        print("color no reconocido")
