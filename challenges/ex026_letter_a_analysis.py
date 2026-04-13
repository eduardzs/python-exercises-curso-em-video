phrase = str(input("Digite uma frase: ")).strip().upper()

print(
    "A letra A aparece {} vezes na frase.\nA primeira letra A apareceu na posição {}.\nA última letra A apareceu na posição {}.".format(
        phrase.count("A"),
        phrase.find("A") + 1,
        phrase.rfind("A") + 1,
    )
)
