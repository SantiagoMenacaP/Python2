print ("Métodos de envío")
print ("GET")
print ("POST")
print ("PUT")
print ("DELETE")
print ("salir")

opc = (input ("Ingrese su opción ")).upper()
if opc == "GET":
  print ("Fetcging resource ...")
elif opc =="POST":
  print ("Creating resource")
elif opc =="PUT":
  print ("Updating resource")
elif opc =="DELETE":
  print ("Deleting resource")    
else :
  print ("usted va a salir")