def suma (a, b):
    # definir la condicion de stop
    if b == 0:
        return a

    # Reglas de recursividad
    return 1 + suma(a, b-1)


