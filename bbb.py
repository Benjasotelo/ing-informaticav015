#
# Ingrese el nombre y la edad de los pacientes
# el nombre debe ser : , no vacio y distinto de "puros espacios"
# la edad debe ser un numero , mayor que 0 y menor o igual a 120 años
# Si edad es mayor o igual que 60 decir: "tiene 60 o mas años "
# Si edad es menor a 60 decir "tiene menos de 60 años"
# Repetir hasta que el usuario indique no desea ingresar más pacientes
# Al final, deberá mostrar LA LISTA con los nombres de los pacientes de mas de 60
# importante : no puede haber dos pacientes con el mismo nombre (repetido)

from time import sleep
carrito=[]  # define una lista vacia

for i in range(5):
    producto = input("ingrese algo : ")
    if producto not in carrito :
        carrito.append(producto)
    else :
        print("sorry, el carrito ya contiene ese producto")
        
# fin del for

for producto in carrito :
    print(producto)
    sleep(1)
# fin del for

miset={}
midict={}
milista=[]

nombre='juan'
edad = 70

mitupla=(nombre,edad)

miset.add(mitupla)
midict[nombre]=edad
milista.append(mitupla)