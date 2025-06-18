#Validaciones.py
minlen = 8
maxlen = 16

def validar(txt):

    valido = False
    
    num = 0
    minu = 0
    mayu = 0
    spec = 0
    error = 0
    
    print(txt)

    if ( len(txt) >= 8 and len(txt) <= 16 ) :
        print(1)
        if " " not in txt :
            print(2)
            for l in txt :
                print(l)
                if   l in '0123456789':
                    num += 1
                elif l in 'abcdefghijklmnopqrstuvwxyz' :
                    minu += 1     
                elif l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
                    mayu += 1
                elif l in "$#_-?&+-*/" :
                    spec += 1
                else : 
                    error += 1  # contiene otros caracteres que no son validos o no están permitidos
            if num > 0 and minu > 0 and mayu > 0 and spec > 0 and error == 0:
                valido = True

    return valido

# inicio

print("Una contraseña segura debe ")
print(f"* tener entre {minlen} y {maxlen} caracteres")
print("* contener al menos 1 numero (0-9)")
print("* contener al menos 1 mayúscula (A-Z)")
print("* contener al menos 1 minúscula (a-z)")
print("* contenar al menos uno de los siguientes caracteres especiales : $#_-?&+-*/ ")
print("* no contenar NINGUN espacio en blanco, NI Ñ o ñ, ni vocal con tildes")

password = input("ingrese una contraseña segura:")

if validar(password) :
    print("Cumple con todas las condiciones")
else :
    print("No es una contraseña segura ")
