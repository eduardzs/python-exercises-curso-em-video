print("-=-" * 25)

numero = int(input("Digite um número inteiro: "))

print("-=-" * 25)
print("Escolha Uma Das Bases Para Conversão")
print("-=-" * 25)
print("[1] Converter Para BINÁRIO")
print("[2] Converter Para OCTAL")
print("[3] Converter Para HEXADECIMAL")
print("-=-" * 25)

escolha = int(input("Sua Opção: "))

print("-=-" * 25)

if escolha == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, bin(numero)[2:]))
elif escolha == 2:
    print("{} convertido para OCTAL é igual a {}".format(numero, oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hex(numero)[2:]))
else:
    print("Opção Inválida. Tente Novamente!")
    print("ENCERRANDO O PROGRAMA...")

print("-=-" * 25)
