print("-=-" * 25)
print("Analisador de Triângulos")
print("-=-" * 25)

a = float(input("Primeiro Segmento: "))
b = float(input("Segundo Segmento: "))
c = float(input("Terceiro Segmento: "))

if a + b > c and a + c > b and b + c > a:
    print("Os segmentos acima PODEM FORMAR triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")
