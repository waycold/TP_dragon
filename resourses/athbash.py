def cifrado_atbash(cadena):
    i = 0
    cadenita = ""
    abecedario = {"a":["z","Z"],"b":["y","Y"],"c":["x","X"],"d":["w","W"],
                  "e":["v","V"],"f":["u","U"],"g":["t","T"],"h":["s","S"],
                  "i":["r","R"],"j":["q","Q"],"k":["p","P"],"l":["o","O"],
                  "m":["ñ","Ñ"],"n":["n","N"],"ñ":["m","M"],"o":["l","L"],
                  "p":["k","K"],"q":["j","J"],"r":["i","I"],"s":["h","H"],
                  "t":["g","G"],"u":["f","F"],"v":["e","E"],"w":["d","D"],
                  "x":["c","C"],"y":["b","B"],"z":["a","A"],}
    numeros = {"1":"9","2":"8","3":"7","4":"6","5":"5","6":"4","7":"3","8":"2","9":"1",}
    while i<len(cadena):
        if cadena[i].isalpha():
            if cadena[i].isupper():
                cadenita+= abecedario[cadena[i].lower()][0]
            else:
                cadenita+= abecedario[cadena[i]][1]

        elif cadena[i].isdigit():
            cadenita += numeros[cadena[i]]
        else:
            cadenita+=cadena[i][0]
        i+=1
    return cadenita