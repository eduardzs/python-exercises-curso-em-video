numero = int(input("Digite um número: "))

print(
    "O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.".format(
        numero, (numero * 2), numero, (numero * 3), numero, (numero ** (1 / 2))
    )
)
