"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    sum = 0 
    for i in range(1, n+ 1):
        sum += i
    return sum 

    


def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n <= 1:
        return n 
    return (n + suma_recursiva(n -1))
    

n = 5 
r1 = suma_ciclo(n)
r2 = suma_recursiva(n)
print("prueba: " ,n )
print("ciclo: ", suma_ciclo)
print("recu: ", suma_recursiva)