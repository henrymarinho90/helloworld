sumaPares=0;
n=int(input('Ingrese el limite superior para la suma de números pares'))
for i in range(0,n+1):
    if(i%2==0):
        sumaPares=sumaPares+i
        
        print('La suma de los numeros pares en el rango establecido es: ', sumaPares);
