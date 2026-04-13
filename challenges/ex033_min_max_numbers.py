valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo Valor: "))
valor3 = int(input("Terceiro Valor: "))

maior = valor1
menor = valor1

if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3

print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}".format(menor))
