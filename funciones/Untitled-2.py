def menu():
    print("1.- hacer alguna cosita\n2.-imprimir alguna cosita \n0.- salir")
    return ( input("ingrese opcion : ") )

def hacer_algo():
    for i in range(10):
        print(i)

def hacer_otra_cosa():
    print("fin fin fin")

# programa principal inicia aqui
opcion = ''
while opcion != 'salir' :
    
    opcion = menu()
    
    if opcion == '1':
        hacer_algo()
    elif opcion == '2':
        hacer_otra_cosa()
    elif opcion == '0':
        opcion ='salir'
    else :
        print("opcion no valida")
print("***")

