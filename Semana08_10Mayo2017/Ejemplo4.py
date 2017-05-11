def invertirCadena(s):
    # Condicion de stop
    if s == "":
        return s

    # Codigo de recursividad
    return invertirCadena(s[1:]) + s[0]


print (invertirCadena("UTEC"))