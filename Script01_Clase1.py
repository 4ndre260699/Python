### Numpy ###

import numpy as np

import random as rnd

# help(np) (comentado por ser muy largo)

# Funcion dir : Listar los componentes del modulo

# print(dir(np)) (comentado por ser muy largo)

### Primeros Pasos ###

#help(np.array) (comentado por ser muy largo)

# Definimos una lista

Lista1 = [12,13,24,3465,576,457,5678,567,56,765]
Vec1 = np.array(Lista1)
print(Vec1)

# Tipo de lista

print(type(Lista1))

# Tipo de datos de Vec1

print(type(Vec1))

# Lista de metodos/atributos que podemos aplicar a un dato de tipo numpy.ndarray

# print(dir(Vec1)) (comentado por ser muy largo)

# Generemos un conjunto de notas aleatorias

notas = []
for n in range(10000):
    notas.append(rnd.randint(0,20))

# Notas simuladas
# print(notas) (comentado por ser muy largo)

# El objeto notas lo puedo transformar a un objeto ndarray

notas = np.array(notas)

# np.array proviene de una lista

print(len(notas))

# Calcular la suma de todas las notas

print(sum(notas))

# Calcular el promedio

promedioNotas = sum(notas)/len(notas)

print(promedioNotas)

# Repliquemos 1000 veces el siguiente experimento : Generar un vector con 10000 notas

# Definamos una funcion que devuelve el vector de notas (10000 elementos)}

def SimulNotas(Num = 10000) :
    notas = []
    for i in range(Num) :
        notas.append(rnd.randint(0,20))
    return np.array(notas)

# Ejecutemos la funcion SimulNotas un numero total de 1000 veces
# y guardemos los promedios de estas 1000 ejecuciones
# Miramos el tiempo de esta ejecucion

Prom = list()

# Crear un directorio donde almacenaremos todos nuestros archivos simulados

import os

os.mkdir("TLC1")



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import time
IniciaCronometro = time.time()

for exe in range (1000) : 
    notas = SimulNotas()
    Promedio = sum(notas)/len(notas)

    # Guardemos estos promedios de una lista
    
    Prom.append(Promedio)

    # Guardemos en Disco Duro ese vector : Empezamos creando un nombre de archivo que diferencia a cada archivo generado (IMPORTANTE)

    nombre_archivo = "TLC1/" + "Prom" + "iter" + str(exe) + ".txt"

    np.savetxt(nombre_archivo, Prom)

FinalizaCronometro = time.time()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Calculemos la media de Prom

print("""
La media de 1000 ejecuciones es: %.3f
Timpo de ejecucion : %d
"""%(sum(Prom)/len(Prom), FinalizaCronometro-IniciaCronometro))

# Operaciones con objetos de tipo ndarray

# Ya sabemos que es un iterable

for elemento in np.array([12,4,2,9]) :
    print(elemento**2)

# Acceso a los elementos de un adarray

# primer elemento de notas
print(notas[0])
# Ultimo elemento de notas
print(notas[-1])
# Primeros 5 elementos de notas
print(type(notas[:5]))
# Ultimos 8 elementos de notas
print(notas[-8:])
# Del 10mo elemento al 20avo elemento de notas
print(notas[9:20])

# Atributos informativos de un ndarray

# El atributo shape
print(notas.shape)

# Documentacion de la funcion np.array
# print(help(np.array))