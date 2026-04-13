temperatura = float(input("Informe a temperatura em ºC: "))

print(
    "A temperatura de {}ºC corresponde a {:.1f}ºF.".format(
        temperatura, (9 / 5 * temperatura + 32)
    )
)
