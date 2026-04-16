from datetime import date

ano = int(input("Ano de Nascimento: "))

print("INFORME SEU SEXO")
print("[ 1 ] MASCULINO")
print("[ 2 ] FEMININO")

sexo = int(input("Selecione uma das opções acima: "))

ano_atual = date.today().year
idade = ano_atual - ano

if sexo == 1:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, ano_atual))
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!.")
    elif idade < 18:
        print("Ainda faltam {} anos para o alistamento.".format(18 - idade))
        print("Seu alistamento será em {}.".format(ano_atual + (18 - idade)))
    else:
        print("Você já deveria ter se alistado há {} anos.".format(idade - 18))
        print("Seu alistamento foi em {}.".format(ano_atual - (idade - 18)))
elif sexo == 2:
    print("Você NÃO precisa se alistar.")
else:
    print("OPÇÃO INVÁLIDA!")
    print("ENCERANDO O PROGRAMA...")
