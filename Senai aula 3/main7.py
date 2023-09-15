# Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.
codigo_area = input("Digite o código de área: ")
numero = input("Digite o número principal: ")

numero_completo = f"+{codigo_area} {numero}"

print(numero_completo)
