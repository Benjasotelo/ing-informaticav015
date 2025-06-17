
def fnCuadrado():
    print("ha seleccionado Cuadrado")
    try :
        lado = float ( input("se requiere la medida del lado (en cms) : ") )
    except :
        print("error, se esperaba un numero")
    else :
        if lado <= 0 :
            print("error, se esperaba un numero mayor que 0")
        else :
            P = round ( 4 * lado , 2 )
            A = round ( lado * lado , 2 ) # lado ** 2  # lado ^ 2
            print(f"el área es {A} cm2 y el perimetro es {P} cms")
    
    
def fnRectangulo():
    print("ha seleccionado Rectangulo")
    try :
        ladoA = float ( input("se requiere la medida del lado 1 (en cms) : ") )
        ladoB = float ( input("se requiere la medida del lado 2 (en cms) : ") )
    except :
        print("error, se esperaban valores numericos")
    else :
        if ladoA <= 0 or ladoB <= 0:
            print("error, se esperaban números mayores que 0")
        else :
            P = round ( 2 * ( ladoA + ladoB ) , 2 )
            A = round ( ladoA * ladoB , 2 ) # lado ** 2  # lado ^ 2
            print(f"el área es {A} cm2 y el perimetro es {P} cms")
        
def fnTriangulo():
    print("ha seleccionado Triangulo")
    try :
        ladoA = float ( input("se requiere la medida del lado 1 (en cms) : ") )
        ladoB = float ( input("se requiere la medida del lado 2 (en cms) : ") )
        ladoC = float ( input("se requiere la medida del lado 3 (en cms) : ") )
    except :
        print("error, se esperaban valores numericos")
    else :
        if ladoA <= 0 or ladoB <= 0:
            print("error, se esperaban números mayores que 0")
        else :
            P = round ( ladoA + ladoB + ladoC  , 2 )
            S = P/2
            A = round ( sqrt( S * (S-ladoA) * (S-ladoB) * (S-ladoC) ) , 2 ) 
            print(f"el área es {A} cm2 y el perimetro es {P} cms")    
    
def fnCirculo():
    print("ha seleccionado Circulo")
    try :
        radio = float ( input("se requiere la medida del radio (en cms) : ") )
    except :
        print("error, se esperaba un numero")
    else :
        if radio <= 0 :
            print("error, se esperaba un numero mayor que 0")
        else :
            P = round ( 2 * pi * radio , 2 )
            A = round ( pi * ( radio ** 2 ) , 2 ) 
            print(f"el área es {A} cm2 y el perimetro es {P} cms")

from os import system
from time import sleep
from math import pi, sqrt 

Repetir = True

while Repetir :
    system("cls")
    
    print("Menu\n----\n1.-Cuadrado\n2.-Rectangulo\n3.-Triangulo\n4.-Circulo\n9.-Salir")
    
    op = input("ingrese su opcion :")
    
    if op == '1' :
        fnCuadrado()
    elif op == '2' :
        fnRectangulo()
    elif op == '3' :
        fnTriangulo()
    elif op == '4' :
        fnCirculo()
    elif op == '9' :
        Repetir = False
    else :        
        print("la opción ingresada no es valida")
        
    #sleep(2)
    input("\npress any key to continue ....")
print("***")
