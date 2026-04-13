from random import choice

aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))

print("O aluno escolhido foi {}!".format(choice([aluno1, aluno2, aluno3, aluno4])))
