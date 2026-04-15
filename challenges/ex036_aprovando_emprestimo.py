casa = float(input("Valor da Casa: R$ "))
salario = float(input("Salário do Comprador: R$ "))
anos = int(input("Quantos Anos de Financiamento? "))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(
    "Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.".format(
        casa, anos, prestacao
    )
)

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
