'''
Created on 24 oct 2024

@author: carlo
'''
#ejercicio A



def P2(n, k, i=1):
    
    if not (isinstance(n, int) and isinstance(k, int) and isinstance(i, int)):
        return ValueError
    if n < 0 or k < 0 or i < 0:
        return ValueError
    if i >= k + 1:
        return ValueError
    if n < k:
        return ValueError
    
    resultado = 1
    for i in range(i, k + 1):  
        resultado *= (n - i + 1)
    
    return resultado
print(P2(2,0,1))

#ejercicio B



import math

def C2(n, k):
  
    if not (isinstance(n, int) and isinstance(k, int)):
        return  ValueError
    if n <= 0 or k < 0:
        return  ValueError
    if n <= k:
        return  ValueError
    
 
    return math.factorial(n) // (math.factorial(k + 1) * math.factorial(n - (k + 1)))


print(C2(4, 2))  

#ejercicio C
import math

def combinatorio(n, k):
    
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def S2(n, k):
    
    
    
    if not (isinstance(n, int) and isinstance(k, int)):
        return ValueError
    if n < 0 or k < 0:
        return 
    if n < k:
        return ValueError
    
    factorial_k = math.factorial(k)
    factorial_k_plus_2 = math.factorial(k + 2)
    
    suma = 0
    
    for i in range(k + 1):  
        signo = (-1) ** i  
        combinatorio_binomial = combinatorio(k, i)  
        termino_potencia = (k - i) ** (n + 1)  
        suma += signo * combinatorio_binomial * termino_potencia  

    resultado = (factorial_k * suma) / (n * factorial_k_plus_2)
    
    return resultado

print(S2(4, 2))  

#ejercicio D
from collections import Counter
from typing import List, Tuple

def palabrasMasComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
   
    if n < 1:
        return ValueError
    
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contenido = file.read()
            
            contenido = contenido.lower()
            
            palabras = contenido.split()
            
            contador_palabras = Counter(palabras)
            
            palabras_comunes = contador_palabras.most_common(n)
            
            return palabras_comunes
    
    except FileNotFoundError:
        return f"El archivo {fichero} no fue encontrado."


nombre_fichero = "archivo_palabras.txt"
resultado = palabrasMasComunes(nombre_fichero, 3)

print(f'Las palabras más comunes en el archivo "{nombre_fichero}" son:')
print(resultado)

#ejercicio E
def prueba_P2():
    print("\nPruebas para la función P2:")
    try:
        assert P2(4, 2, 1) == 12, "Error en P2(4, 2, 1)"
        assert P2(5, 3, 2) == 30, "Error en P2(5, 3, 2)"
        assert P2(5, 3, 5) == ValueError, "Error en P2(5, 3, 5)"
        assert P2(4, 5, 1) == ValueError, "Error en P2(4, 5, 1)"
        assert P2(-1, 2, 1) == ValueError, "Error en P2(-1, 2, 1)"
        assert P2(4, -2, 1) == ValueError, "Error en P2(4, -2, 1)"
        assert P2(4, 2, -1) == ValueError, "Error en P2(4, 2, -1)"
        assert P2(4, 2, 5) == ValueError, "Error en P2(4, 2, 5)"
     
    except Exception as e:
        print("Error en P2:", e)

def prueba_C2():
    print("\nPruebas para la función C2:")
    try:
        assert C2(4, 2) == 3, "Error en C2(4, 2)"
        assert C2(4, 5) == ValueError, "Error en C2(4, 5)"
        assert C2(4, -1) == ValueError, "Error en C2(4, -1)"
        assert C2(-4, 2) == ValueError, "Error en C2(-4, 2)"
       
    except Exception as e:
        print("Error en C2:", e)

def prueba_S2():
    print("\nPruebas para la función S2:")
    try:
        assert S2(4, 2) is not None, "Error en S2(4, 2)"
        assert S2(4, 5) == ValueError, "Error en S2(4, 5)"
        assert S2(-4, 2) == ValueError, "Error en S2(-4, 2)"
        assert S2(4, -2) == ValueError, "Error en S2(4, -2)"
        assert S2(4, 'dos') == ValueError, "Error en S2(4, 'dos')"
      
    except Exception as e:
        print("Error en S2:", e)

def prueba_palabrasMasComunes():
    print("\nPruebas para la función palabrasMasComunes:")
    try:
        
        resultado = palabrasMasComunes('archivo_palabras.txt', 3)
        print("Las 3 palabras más comunes:", resultado)
        assert palabrasMasComunes('archivo_palabras.txt', 1) is not None, "Error en n=1"
        assert palabrasMasComunes('archivo_palabras.txt', 0) == ValueError, "Error en n=0"
        assert palabrasMasComunes('archivo_palabras.txt', -1) == ValueError, "Error en n=-1"
        assert palabrasMasComunes('archivo_inexistente.txt', 3) ==  "Error en archivo no encontrado"
        
    except Exception as e:
        print("Error en palabrasMasComunes:", e)


def ejecutar_pruebas():
    prueba_P2()
    prueba_C2()
    prueba_S2()
    prueba_palabrasMasComunes()

print(ejecutar_pruebas())


   




    
