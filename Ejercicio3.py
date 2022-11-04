#Funcion para Crear la matriz

def matrizKreator(n,m):
    A=[]
    for i in range(n):
        A.append([])
        for j in range(m):
            A[i].append(int(input("Ingrese la duracion de llamada en segundos: ")))
    return(A);

#Funcion para calcular el promedio de la matriz
def prom(A):
    Agente=0
    suma=0
    for i in A:
        for j in i:
            suma+=j
            Agente+=1
    return suma/Agente

#Definir tamaño del vector
n = int(input("Ingrese el numero de agentes: "));
m = int(input("Ingrese el numero de llamadas por agente: "))

#Mostrar la matriz creada
Matrix=matrizKreator(n,m)
print("La matriz creada es la siguiente: ", Matrix, end= " ")

#Calcular el promedio
Promedio=prom(Matrix)
print("El promedio de la matriz creada es el siguiente: ", Promedio, end= " ")
