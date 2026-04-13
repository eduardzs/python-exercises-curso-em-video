from random import randint
from time import sleep

jogador = int(input("Em que número eu pensei? "))
computador = randint(0, 5)

print("-=-" * 25)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 25)

print("PROCESSANDO...")
sleep(1.5)

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))
