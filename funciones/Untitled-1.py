# aqui defino las funciones
def imprime_hacia_abajo():
    for i in "hola mundo" :
        print(i)

def imprime_al_reves(texto="valor por defecto"):
        print(texto[::-1])

def duplicador(numero):
    return numero*2


# aqui comienza mi programa principal y llamo a las funciones

#imprime_hacia_abajo()
imprime_al_reves("hello")

imprime_al_reves()

j=duplicador(17)
print(f"el doble de 17 es {j}")

try:
    a=int(input("ingrese un numero : "))    
except :
    print("te dije un numero")
else :
    b = duplicador(a)
    print(f"el doble de {a} es {b}")
    
