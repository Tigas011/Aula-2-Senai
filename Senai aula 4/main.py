# Exercício 1: Verificação de Número Positivo

# n1 = float(input("Digite um número "))
# if n1 > 0:
#     print("O número {} é positivo.".format(n1))
# elif n1 < 0:
#     print("O número {} é negativo".format(n1))
# else:
#     print ("O número {} é zero".format(n1))


# Exercício 2: Classificação de Triângulos

a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

if a == b == c:
    print("O triângulo é equilátero.")

elif a == b or a == c or b == c:
    print("O triângulo é isósceles.")

else:
    print("O triângulo é escaleno.")




