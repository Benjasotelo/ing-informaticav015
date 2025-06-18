from os import system

mas_de_sesenta ={} # diccionario_vacio
total_pacientes = 0 
total_tatitas = 0

Repetir = True

while Repetir :
    system("cls")
    #----
    nombre = None
    
    nombre = input("ingrese nombre y apellidos del paciente :").lower()
    if nombre == None or nombre == ''  :
        print("el nombre ingresado no es válido")
    elif nombre in mas_de_sesenta :
        print("el nombre ingresado ya existe")
    else :
        try :
            edad = int( input("ingrese la edad del paciente :") )
        except :
            print("error, se esperaba un número ")
        else : 
            if edad <= 0 or edad >= 120 :
                print("error, se esperaba un número entre 0 y 120 años ")
            elif edad >= 60 :
                total_pacientes += 1
                total_tatitas += 1
                print("60 o mas años")
                mas_de_sesenta[nombre]=edad  # uso nombre como clave y edad como valor
            else :
                total_pacientes += 1
                print("menos de 60")
                
    #----
    aux = input("Desea ingresar otro ? (Si/No) : ").lower()
    if aux == "no" :
        Repetir = False
        
print("...")

print(f"se registraron : {total_pacientes}")
print(f"de los cuales {total_tatitas} tiene 60 o más años")
print("estos pacientes son :")

for paciente in mas_de_sesenta :
    print(paciente, paciente[edad])

#print(mas_de_sesenta)

print("***")
    
    







