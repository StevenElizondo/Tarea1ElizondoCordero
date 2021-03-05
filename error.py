def funcionErr():
    # error detectable por flake8: falta espacio entre operador
    i=0
    while(true):
        i = i+1
    # error detectable por flake8: sintaxis erronea es doble igual
    if(i=4):
        # error detectable por flake8: falta espacio despues de la coma
        print("hola mundo ",f)   