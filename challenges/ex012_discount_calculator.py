preco = float(input("Informe o preço do produto: R$"))

print(
    "Preço Original: R${:.2f}\nDesconto (5%): R${:.2f}\nPreço com Desconto: R${:.2f}".format(
        preco, (preco * 5 / 100), (preco - (preco * 5 / 100))
    )
)
