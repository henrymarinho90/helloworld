def primo(n):
    for i in range(2,int(n/2)):
        if(n%i==0):
            return False;
    return True

Arr=[13,12,27,31,56,11,10]
for i in Arr:
    if(primo(i)):
        print("El numero ", i," es primo")
    else: print("El numero ", i," NO es primo")

