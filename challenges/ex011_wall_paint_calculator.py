largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

print(
    "Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m².\nPara pintar essa parede, você precisará de {:.2f}L de tinta.".format(
        largura, altura, (largura * altura), ((largura * altura) / 2)
    )
)
