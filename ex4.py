# -*- coding: utf-8 -*-
'''
Este código nos permite codifucar una secuencia de bits (también funciona con letras)
a través del método de Run length. La entrada para la funcion es un array alfanumérico.
Ref:
    https://www.geeksforgeeks.org/run-length-encoding-python/
'''


def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message)-1):
        count = 1  # inicializamos el contador
        ch = message[i]  # extraemos el caracter de la string
        j = i  # inicializamos el contador del bucle
        while (j < len(message)-1):  # mientras el caracter actual sea igual a los siguientes, vamos aumentando count
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break  # si el caracter actual no es igual al que estamos comparando, salimos del bucle
        encoded_message = encoded_message+str(count)+ch  # Añadimos a la string el caracter y las repeticiones
        i = j+1  # saltamos todos los caracteres repetidos y vamos al siguiente
    return encoded_message


encoded_message = encode("000001000011000111001111011111")
print(encoded_message)
