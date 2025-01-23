# Consideraciones importantes y sintaxis de python

# Función con bucle for y condicional if-else

def imprimir_numeros_pares_hasta_n(n):
    """
    Imprime todos los números pares desde 0 hasta el número n (incluido).
    """
    for i in range(n+1):
        if i % 2 == 0: # Verifica si el numero es par 
            print(i)
        else:
            print(f"{i}  (Impar)")

# Uso de la función

limite = 1000000
print(f"Números pares hasta {limite}:")
imprimir_numeros_pares_hasta_n(limite)

"""
En esta función, se utiliza un bucle for para recorrer todos los números desde 0 hasta n (incluido).
Dentro del bucle, se utiliza un condicional if-else para verificar si el número actual es par o impar.
Si el número es par (es decir, el resto de la división por 2 es 0), se imprime el número.

"""
