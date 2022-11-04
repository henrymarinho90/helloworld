A=[85,25,37,54,83,98,12]
def funcion(A):
    str_pos=""
    for i in A:
        if(i%2==1 or i%10==5):
            str_pos=str_pos+str(i)+ " "
    return str_pos
m=funcion(A)
print(m)


def Mistery(n):
    i=0
    a=0
    while(i<n):
        a=a+i
        i=i+2
    return a
misterio=Mistery(5)
print(misterio);