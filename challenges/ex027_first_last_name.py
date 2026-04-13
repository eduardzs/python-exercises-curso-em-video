name = str(input("Digite seu nome completo: ")).strip()

print(
    "Muito prazer em te conhecer!\nSeu primeiro nome é {}.\nSeu último nome é {}.".format(
        name.split()[0], name.split()[-1]
    )
)
