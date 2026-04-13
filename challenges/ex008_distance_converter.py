x = float(input("Digite uma distância em metros: "))

print(
    "A distância de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm".format(
        x, (x / 1000), (x / 100), (x / 10), (x * 10), (x * 100), (x * 1000)
    )
)
