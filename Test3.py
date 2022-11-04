M=[[1,2,3],[4,5,6],[7,8,9]]
a=50
for i in range(len(M)):
    for j in range(len(M)):
        M[i][j]= 10 % (i+j+6)
print(M);
