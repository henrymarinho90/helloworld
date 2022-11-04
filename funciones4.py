Arreglo=[23,25,24,48,26,45,56,48,67]
def mayor_arreglo(A):
    mayor=A[0]
    for i in range(len(A)):
        if(mayor< A[i]):
            mayor=A[i]
    return mayor
print("El mayor del arreglo es: ", mayor_arreglo(Arreglo));
