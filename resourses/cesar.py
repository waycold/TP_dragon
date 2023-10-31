def cifrado_cesar(cadena,clave):
    lista=[]
    i=0
    cadena_nueva="" 
    while i<len(cadena):
        if cadena[i].isalpha():
            cadena_nueva+= chr(ord(cadena[i])+clave)
        elif cadena[i].isdigit():
            cadena_nueva+= str(int(cadena[i])+clave)
        else:
            cadena_nueva+=cadena[i]
        i+=1
    return cadena_nueva

print(cifrado_cesar(111,2))