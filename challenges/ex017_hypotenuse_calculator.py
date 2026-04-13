from math import hypot

oposto = float(input("Comprimento do Cateto Oposto: "))
adjacente = float(input("Comprimento do Cateto Adjacente: "))

print("A hipotenusa vai medir {:.2f}".format(hypot(oposto, adjacente)))
