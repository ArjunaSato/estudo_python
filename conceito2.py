nota1=input("Digite a primeira nota: ")
nota2=input("Digite a segunda nota: ")
nota3=input("Digite a terceira nota: ")
nota4=input("Digite a quarta nota ")

# Vamos converter as variáveis de notas do tipo str para o tipo float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1+nota2+nota3+nota4) / 4

# Se a nota média do aluno for maior ou igual a 7, ->aprovado
# Senão se a nota média do aluno for menos ou igual a 4, -> Reprovado
# senão, -> Recuperação

if media>=7:
    print("Sua nota média é"+ str(media) +"Aprovado")
elif media<=4:
    print("Sua nota média é"+str(media)+"Reprovado")
else:
    print("Sua nota média é"+str(media)+"\n Você Recuperação")




    