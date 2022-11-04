V=[1,7,13,15,21,26,39];
Modulos713=[];
for i in range(len(V)):
    if (V[i]%7==0) or (V[i]%13==0):
        Modulos713.append(V[i]);
print(Modulos713)