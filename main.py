# función para verificar si se pasó un único caracter 
def check_char(parm):
    if type(parm) == str or type(parm) == chr:
        # si es un unico caracter entre A-Z/a-z   
        if (len(parm) == 1 and parm.isalpha()):  
            return 0
        # si son mas de un caracter entre A-Z/a-z
        elif (len(parm) > 1 and parm.isalpha()):  
            return -1
        # si son uno o mas y ademas contiene no alfabéticos
        elif (len(parm) >= 1 and (not parm.isalpha())):  
            return -2
    else:   
        return -3   # si no es string o char


# función para cambiar el case de un char 
def caps_switch(parm):
    res = check_char(parm)  
    # guarda la consulta en una variable para no llamar la funcion cada vez
    if(res == 0):   # si es un único caracter alfabético
        if(parm.isupper()):  # es esta en mayusculas
            return parm.lower()  # retorna minusculas
        else:   # si no
            return parm.upper()  # retorna mayusculas
    else:   # si no es válido
        # retorna el valor de error segun el resultado de check_char
        return res  