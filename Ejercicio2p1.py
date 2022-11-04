V=[9,12,15,18,2,45,33];
Vpar=[]
Vimpar=[]
print(V)
for i in range(len(V)-1):
    for j in range(len(V)-1-i):
        if (V[j+1]<V[j]):
                aux=V[j]
                V[j]=V[j+1]
                V[j+1]=aux;
print(V);
for i in range(len(V)):
    if (V[i]%2==0):
        Vpar.append(V[i])
    else: Vimpar.append(V[i])
print(Vpar);
print(Vimpar);
V=Vpar+Vimpar
print(V);