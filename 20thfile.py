Matriz=[[2,3,1],[4,5,5],[0,7,8]]
print(Matriz)
for i in range(len(Matriz)):
    for j in range(len(Matriz)):
        Matriz[i][j]=i+j
        print(Matriz[i][j], end=" ")
