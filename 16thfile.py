#Creado por Henry Marino AlgoritmoMayoraProm
#Variables
listado=[]
sumaN=0
cantidad=0
mayoresPromedio = []
#Solicitar los numeros
for i in range(100):
    numero=int(input("Ingrese un numero: "))
    sumaN=sumaN+numero
    listado.append(numero)
#Calcular promedio
promedio=sumaN/100
#Calcular mayores al promedio
for i in listado:
    if i>promedio:
        cantidad+=1
        mayoresPromedio.append(i)
#Mostrar valores
print("Existen ", cantidad, "numero mayores al promedio")
print("Los numeros mayores al promedio son: ", mayoresPromedio)
        
