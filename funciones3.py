Arreglo=[23,45,67,78,79,12]
def promedio(Arreglo):
    suma=0
    for i in Arreglo:
        suma=suma+i
    return suma/len(Arreglo)
print("Promedio es igual", promedio(Arreglo));
