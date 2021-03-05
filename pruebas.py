from main import check_char, caps_switch # importa las funciones check_char, caps_switch del archivo negro.py
from string import ascii_lowercase, ascii_uppercase # variables "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "abcdefghijklmnopqrstuvwxyz"

# funcion de testing
def test():
    for c in ascii_uppercase:
        assert check_char(c) == 0 # caso de exito para toda letra c en las mayusculas
    for c in ascii_lowercase:
        assert check_char(c) == 0 # caso de exito para toda letra c en las minusculas
    for c in ascii_uppercase:
        assert caps_switch(c) == c.lower() # caso de exito para toda letra c en las mayusculas, resultado esperado esa misma letra en minuscula
    for c in ascii_lowercase:
        assert caps_switch(c) == c.upper() # caso de exito para toda letra c en las minusculas, resultado esperado esa misma letra en mayuscula
    assert check_char("Aa") == -1 # pureba el punto b de check_char con su codigo unico de error -1
    assert check_char("A.") == -2 # pureba el punto c de check_char con su codigo unico de error -2
    assert check_char(["A",1]) == -3 # pureba el punto d de check_char con su codigo unico de error -3

