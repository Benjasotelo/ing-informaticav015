# aqui se ponen las funciones

# ----------------------------------
def mostrar_menu( lista ) :
    op = 1
    print()

    for elemento in lista :
        print(f"\t{op}.- {elemento}")
        op += 1 

    print( f"\t0.- salir\n")

# ----------------------------------

# arriba los import

from os import system
from time import sleep
from random import randint

# aqui el codigo principal

system("cls")  # limpiar la pantalla

print("calcula promedios")

# ---------------------------------------------
# 1.1. ingresar el nombre de la asignatura
# ---------------------------------------------
'''
while True :
    asignatura = input("ingrese nombre de la asignatura : ").strip().lower() 
    if asignatura == None or asignatura == '' :
        print("nombre no valido, reintente")
    else :
        break
print(f"-{asignatura}-")
'''
# ---------------------------------------------


# -----------------------------------------------------------------
# 1.1. ingresar el nombre de la asignatura, asegurarse que existe
# -----------------------------------------------------------------
'''
lista_asignaturas = ["matemagicas","lenguaje","cloud","progra","innovacion"]

while True :
    asignatura = input("ingrese nombre de la asignatura : ").strip().lower() 
    if asignatura == None or asignatura == '' :
        print("nombre no valido, reintente")
    else :
        if asignatura in lista_asignaturas :
            break
        else :
            print("asignatura ingresada no existe, reintente")
            
print(f"-{asignatura}-")
'''
# ---------------------------------------------

lista_asignaturas = ["matemagicas","lenguaje","cloud","progra","innovacion"]
comidas_tipicas = ["porotos con rienda", "charquican", "sopaipillas","cebiche","cachapas","tequeños","cazuela","pastel de choclo"]

while True :
    mostrar_menu(lista_asignaturas) 
    aux = input("\nseleccione asignatura : ").strip()
    try :
        pos = int(aux) - 1
    except :
        print("opcion no valida, reintente")
    else :
        
        if pos < 0 :
            print("bye bye")
            asignatura="salir"
            break
        elif pos >= len(lista_asignaturas) :
            print("asignatura no valida, reintente")
        else:
            asignatura = lista_asignaturas[pos]
            print(f"-{asignatura}-")
            break
            
# ------------------------------------------------------------------------
#  1.2 Ingresar la cantidad de NOTAS y validar que sea un numero positivo           
# ------------------------------------------------------------------------
if asignatura != "salir " :  # continuo con el programa

    minimo = 0
    maximo = 6
    while True :
        try :
            cant_notas = int( input("\ncantidad de notas : ").strip() ) 
        except :
            print("la cantidad no es valida, se esperaba un numero")
        else :
            if cant_notas > minimo and cant_notas < maximo :
                break
            else :
                print("la cantidad no es valida, intente un valor entre {minimo} y {maximo} ")
            
#---------------------------------------------------
# 1.3 Para cada nota ingresar una ponderacion
#     validar que cada una sea positiva y que la suma
#     total sea un 100%  
#---------------------------------------------------

#------------------------------------------------------------------
# 1.4 Pedir la cantidad de Alumnos (validar que sea mayor que 0)
#------------------------------------------------------------------

#------------------------------------------------------------
# 1.5 Para cada alumno ingresar sus datos :
# Nombres
# Apellidos
# Notas ( para cada prueba, validando en el rango de 1 a 7 )
#------------------------------------------------------------

#-----------------------------------------------------------        
# 1.6 Calcular el promedio ponderado de cada alumnos
#-----------------------------------------------------------        

#-----------------------------------------------------------        
# 1.7 Calcular el promedio general del curso
#-----------------------------------------------------------

#-----------------------------------------------------------
# 1.8 Solicitar la ponderación del Examen Final (ejemplo 40%)
#-----------------------------------------------------------

#-----------------------------------------------------------
# 1.9 Calcular y mostrar la nota minima que cada alumno
# necesita para aprobar la materia
#------------------------------------------------------------

#------------------------------------------------------------
# 2.- GUARDAR LOS DATOS DEL ALUMNO EN DICCIONARIO
# AL FINAL MOSTRAR TODOS
#------------------------------------------------------------
