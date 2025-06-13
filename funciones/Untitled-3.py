# Aqui defino mis funciones y procedimientos
def hola():
    print("hola mundo!")

def saludar(texto):
    print(f"hola {texto}, bienvenid@")

def triple(numero):
    return numero * 3

def alreves(texto="adaN asaP oN"):
    return texto[::-1]

# aqui empieza mi programa principal, llamo a las funciones    
hola() 
nombre = input("como te llamas? : ")
saludar(nombre)
n = 10
t = triple(10)
print(f"sabias que el triple de {n} es {t}")

try:
    n = int(input("ingresa un numero"))
except:
    print("se esperaba un numero")
else :
    print(f"sabias que el triple de {n} es {triple(n)}")

print(alreves(nombre))

print(alreves())



