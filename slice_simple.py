def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
    
    textolower = texto.lower()
    primeras_3 = texto[:3]
    las_del_medio = texto[3:5]
    las4primera = texto[0:4] 
    laantepenultima = texto[-3:]
    lasultimas_letras = las4primera + laantepenultima
    print(primeras_3)
    print(las_del_medio)
    print(lasultimas_letras)
