def slice_advanced():
    # Código a implementar utilizando input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`

        texto = input("Colocar palabra: \n").lower()
        primeras_3 = texto[:3]
        las_del_medio = texto[3:6]
        las4primera = texto[0:4] 
        laantepenultima = texto[-3:]
        lasultimas_letras = las4primera + laantepenultima
        print(primeras_3)
        print(las_del_medio)
        print(lasultimas_letras)
