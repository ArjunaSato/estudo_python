# obter os números pares da lista e somá-los 
num = [34,6,11,19,52,51,58,86,83,92]
resultado=0

for x in num:
    if x%2==0:
        resultado=resultado+x
        print(x)

print("------------------------")
print("O resultado da soma é "+str(resultado))
