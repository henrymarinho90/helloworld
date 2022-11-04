Edades=[12,25,23,18,17,15,15,16];
edad=int(input("Ingrese la edad a buscar: "))
for i in range(len(Edades)):
    if (edad==Edades[i]):
        print("Esa edad existe en el arreglo")
        print("En la posicion: ", i)
    