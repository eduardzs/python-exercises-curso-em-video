seg1 = float(input("Primeiro Segmento: "))
seg2 = float(input("Segundo Segmento: "))
seg3 = float(input("Terceiro Segmento: "))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    if seg1 == seg2 == seg3:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!")
    elif seg1 == seg2 != seg3 or seg1 == seg3 != seg2 or seg2 == seg3 != seg1:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
