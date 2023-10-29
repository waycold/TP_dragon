def cifrado_cesar(mensaje, clave):
    """
    Cifra un mensaje utilizando el cifrado César.

    :param mensaje: Cadena de caracteres a cifrar.
    :param clave: Clave de cifrado (número entero positivo o negativo).
    :return: Mensaje cifrado.

    >>> cifrado_cesar("HOLA", 3)
    'KROD'
    >>> cifrado_cesar("Cifrado Cesar", 7)
    'Jlpavlv Jlzahz'
    >>> cifrado_cesar("Texto de prueba", -13)
    'Grkgb qr cerfn'
    >>> cifrado_cesar("12345", 1)
    '23456'
    >>> cifrado_cesar("abc", 0)
    'abc'
    >>> cifrado_cesar("", 5)
    ''
    >>> cifrado_cesar("Mensaje con espacios", 10)
    'Wyvpnyw myw oczkmsyc'
    >>> cifrado_cesar("Python es genial!", 26)
    'Python es genial!'
    >>> cifrado_cesar("Cifrado Cesar", -3)
    'Zfcoxal Zbpxo'
    >>> cifrado_cesar("abcdefghijklmnopqrstuvwxyz", 25)
    'zabcdefghijklmnopqrstuvwxy'
    """

    cifrado = ""

    for letra in mensaje:
        if letra.isalpha():
            if letra.islower():
                cifrado += chr(((ord(letra) - ord('a') + clave) % 26) + ord('a'))
            elif letra.isupper():
                cifrado += chr(((ord(letra) - ord('A') + clave) % 26) + ord('A'))
        else:
            cifrado += letra

    return cifrado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
