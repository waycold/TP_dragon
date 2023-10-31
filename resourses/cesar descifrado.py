def descifrado_cesar_reverse(cifrado, clave):
    mensaje = ""
    for letra in cifrado:
        if letra.isalpha():
            if letra.islower():
                mensaje += chr(((ord(letra) - ord('a') - clave) % 26) + ord('a'))
            elif letra.isupper():
                mensaje += chr(((ord(letra) - ord('A') - clave) % 26) + ord('A'))
        else:
            mensaje += letra

    return mensaje
