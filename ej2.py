print("Métodos de envío")
print("Get")
print("Post")
print("Put")
print("Delete")
print("Salir")

method = input("Ingrese la opcion: ").capitalize()
match method:
    case "Get":
        print("fetching resourse ...")
    case "Post":
        print("creating resourse ...")
    case "Put":
        print("updating resourse ...")
    case "Delete":
        print("deleting resourse ...")
    case _:
        print("Usted decidió salir")          