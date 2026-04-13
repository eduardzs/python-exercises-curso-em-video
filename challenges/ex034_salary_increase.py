salario = float(input("Qual é o salário do funcionário? R$ "))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)

print(
    "Quem ganhava \033[33m R$ {:.2f}\33[m passa a ganhar \033[32m R$ {:.2f}\33[m agora.".format(
        salario, aumento
    )
)
