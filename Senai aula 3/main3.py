# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
concatenar = str (n1) + str (n2)
print("A  concatenização dos números é: {} e {} é {}" .format(n1,n2,concatenar))