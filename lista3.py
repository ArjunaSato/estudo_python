# obter os números pares da lista e somá-los 
num = [34,6,11,19,52,51,58,86,83,92]
num_par =[]

for x in num:
    if x % 2==0:
        num_par.append(x)
        


# Exibir os valores pares que estão dentro da lista num_par

for i in num_par:
    print(i)