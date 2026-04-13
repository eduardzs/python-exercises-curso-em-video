salario = float(input("Informe o salário atual do funcionário: R$"))

print(
    "Salário Atual: R${:.2f}\nAumento (15%): R${:.2f}\nSalário com Aumento: R${:.2f}".format(
        salario, salario * 15 / 100, salario + (salario * 15 / 100)
    )
)
