from math import cos, sin, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
rad = radians(angulo)

print(
    "O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}".format(
        angulo, sin(rad), angulo, cos(rad), angulo, tan(rad)
    )
)
