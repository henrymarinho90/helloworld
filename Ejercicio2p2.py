V=[9,12,15,18,2,45,33,34];
print(V)
for i in range(0,len(V)-1):
    if (i%2==0):
        aux=V[i]
        V[i]=V[i+1]
        V[i+1]=aux
print(V);