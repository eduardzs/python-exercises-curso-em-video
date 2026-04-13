name = str(input("Digite seu nome completo: ")).strip()

print(
    "Analisando seu nome...\nSeu nome em maiúsculas é {}.\nSeu nome em minúsculas é {}.\nSeu nome tem ao todo {} letras.\nSeu primeiro nome é {} e ele tem {} letras.".format(
        name.upper(),
        name.lower(),
        len(name) - name.count(" "),
        name.split()[0],
        len(name.split()[0]),
    )
)
