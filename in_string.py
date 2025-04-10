def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

    nombre = input("Poner Nombre \n>")
    nombre_minus = nombre.lower()
    
    vocal_a = "a"  in nombre_minus
    vocal_e = "e"  in nombre_minus
    vocal_i = "i"  in nombre_minus
    vocal_o = "o"  in nombre_minus
    vocal_u = "u"  in nombre_minus

    print(vocal_a)
    print(vocal_e)
    print(vocal_i)
    print(vocal_o)
    print(vocal_u)
