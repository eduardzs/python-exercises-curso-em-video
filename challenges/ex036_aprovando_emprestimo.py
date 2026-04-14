casa = float(input("Valor da Casa: "))
salario = float(input("Salário do Comprador: "))
anos = int(input("Quantos Anos de Financiamento? "))

messes = anos * 12
parcela = casa / messes
prestacao = salario * 30 / 100

print(
    "Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}".format(
        casa, anos, parcela
    )
)

if parcela > prestacao:
    print("Empréstimo NEGADO!")
elif parcela < prestacao:
    print("Empréstimo pode ser CONCEDIDO!")
