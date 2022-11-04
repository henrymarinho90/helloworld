import random
A=[]
longArray=0
pares=[]
impares=[]
multiTres=[]
while longArray<=100:
    numero=random.randint(0,100)
    A.append(numero)
    longArray+=1
print(A);
for i in A:
    if (i%2==0):
        pares.append(i)
    else: impares.append(i)
print(pares, end=" ")
print(impares, end=" ")

def prom (B):
    suma=0
    for i in B:
        suma=suma+i
    return suma/len(B)

def multiplosTres(C):
    modulo=0
    for i in C:
        if(i%3==0):
            multiTres.append(i)
    return multiTres


PrintPromP=prom(pares)
PrintPromI=prom(impares)
PrintMultiT=multiplosTres(A)
print("El promedio de los pares es: ", PrintPromP)
print("El promedio de los impares es: ", PrintPromI)
print("Lo: ", PrintMultiT)
