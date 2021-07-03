# El algoritmo del banquero sirve para evitar el abrazo mortal.
# Ejercicio de programación de matrices.
# La entrada del proceso son las estructuras de datos necesarias para que el banquero determine si el sistema está en interbloqueo o está en estado seguro.
# La salida simplemente es mostrar un camino seguro como mínimo. Si no, decir que no hay.


# Explicando las matrices:
# Matriz Existencia: 2 Filas. 1 Fila nombre de recurso. 2 Fila instancias existentes. n°Columnas = n°Recursos.
# Matriz Asignación: n° Filas = n°Procesos, n°Columnas = n°Recursos.
# Matriz Disponible: 2 Filas. 1 Fila nombre de recurso. 2 Fila instancias disponibles luego de asignación. n°Columnas = n°Recursos.
# Matriz Máximo: n° Filas = n°Procesos, n°Columnas = n°Recursos. Es la cantidad máxima que necesita cada proceso de un recurso para terminar normalmente.
# Matriz Necesidad: n° Filas = n°Procesos, n°Columnas = n°Recursos. Diferencia entre máximo y asignación.

from sys import pycache_prefix
import numpy as np
from numpy.lib.function_base import disp

# existencia = np.matrix([[3,14,12,12]])

existencia = np.zeros([4])
print("Introduzca los valores de la matriz EXISTENCIA")
for i in range(4):
    existencia[i] = input("Elemento "+str(i+1)+" ")


# asignacion = np.matrix([
#     [0,0,1,2],
#     [1,0,0,0],
#     [1,3,5,4],
#     [0,6,3,2],
#     [0,0,1,4]
#     ])

asignacion = np.zeros([5,4])
print("Introduzca los valores de Asignacion")
for i in range(5):
    for j in range(4):
        asignacion[i,j] = input("Elemento ["+str(i+1)+","+str(j+1)+"]: ")


# maximo = np.matrix([
#     [0,0,1,2],
#     [1,7,5,0],
#     [2,3,5,6],
#     [0,6,5,2],
#     [0,6,5,6]
#     ])

maximo = np.zeros([5,4])
print("Introduzca los valores de Máximo")
for i in range(5):
    for j in range(4):
        maximo[i,j] = input("Elemento ["+str(i+1)+","+str(j+1)+"]: ")




necesidad = np.zeros([5,4])
procesosTerminados = [0,0,0,0,0]

disponible = np.zeros([4])

asignacionAuxi = np.sum(asignacion,axis=0)

disponible = existencia - asignacionAuxi

necesidad = maximo - asignacion


procesosEnEjecucion = []
orden = []
noConsigueRuta = False

while procesosTerminados != [1,1,1,1,1]:
    for i in range(0,5):
    
        if procesosTerminados[i] == 1:
            continue

        if np.all(necesidad[i] <= disponible):
            print('Proceso ',i+1," se ejecuta")
            procesosEnEjecucion.append(i)
            disponible = disponible - necesidad[i]
            print("Disponible nueva: ", disponible)
        else:
            print('Proceso ',i+1," no se ejecuta, se bloquea.")

    # [0,3]
    for i in procesosEnEjecucion:     
        print("Proceso ", i+1, "terminó.")
        procesosTerminados[i] = 1
        disponible = disponible + maximo[i]
        orden.append(i+1)
        print("Nueva disponible: ", disponible)
        print("Procesos terminados: ", procesosTerminados)   
    
    procesosEnEjecucion.clear()

print("Camino seguro: ", orden)