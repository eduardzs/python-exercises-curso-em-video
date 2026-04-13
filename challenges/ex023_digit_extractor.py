number = int(input("Informe um número: "))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousands = number // 1000 % 10

print(
    "Analisando o número: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(
        number, unit, ten, hundred, thousands
    )
)
