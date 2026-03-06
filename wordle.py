usuario_palabra = ('hoja')
adivinar_la_palabra = ('medir')
intentos = 5
letras_cantidad = 5




def obtener_palabra(usuario_palabra, adivinar_la_palabra):
    cantidad_letras_de_palabra_a_encontrar = 5

    #creamos una lista vacia para almacenar el resultado
    palabra_registrada = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar): #5

        # es ogual el indice 0 de palabra_a_encontrar a indice 0 de palabra_ingresada?
        las_letras_son_iguales = usuario_palabra[posicion] == adivinar_la_palabra[posicion]


        # la letra del indice 0 de palabra_ingresada en la palabra_a_encontrar
        la_letra_existe_en_la_palabra = usuario_palabra[posicion] in adivinar_la_palabra

        if las_letras_son_iguales:
            # si se cumple guardamos en la lista de letras verificadas
            palabra_registrada.append('['+usuario_palabra[posicion]+']')

        elif la_letra_existe_en_la_palabra:
            palabra_registrada.append('('+usuario_palabra[posicion]+')')

        else:
            palabra_registrada.append(usuario_palabra[posicion])

        
    return palabra_registrada

resultado = obtener_palabra('medir' , 'hojas')
print(resultado)