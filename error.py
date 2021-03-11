# ERR8 -5
def funcionErr():
    f = 5
    # error detectable por flake8 corregido: falta espacio entre operador
    i = 0
    while(True):
        i == i+1
    # error detectable por flake8 corregido: sintaxis erronea es doble igual
    if(i == 4):
        # error detectable por flake8 corregido:
        # falta espacio despues de la coma
        print("hola mundo ", f)
