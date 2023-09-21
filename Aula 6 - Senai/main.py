# "COMO CRIAR LISTA USANDO TRUE, APPEND"

lista = [1,3,6,5,5, "casa", 
2.8, True]
print(lista[6])

lista = [1,3.28,-6,5,5, "casa", 2.8, True]
lista.append(9)
print(lista)

# "REMOVE O NUMERO DA LISTA"
lista2 = [1,3,566,545,5646]
lista2.remove(566)
print(lista2)

del lista2[0]
print(lista2)

lista4 = len(lista2)
print(lista4)

lista5 = [1,45,89,78,123,45,78,56]
for i in lista5:
    print(i)

# Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 5 e imprima-a na tela.

numeros = [1,2,3,4,5]
print(numeros)

# Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.

numeros = [1,2,3,4,5]
print(lnumeros[2])

# Exercício 3: Adicione o número 6 à lista `numeros` e imprima a lista atualizada.

lista = [1,2,3,4,5]
lista.append(6)
print(lista)

# Exercício 4: Remova o número 3 da lista numeros e imprima a lista resultante.

numeros = [1,2,3,4,5,6]
numeros.remove(3)
print(numeros)

# Exercício 5: Crie uma lista chamada frutas contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
frutas = ["uva","maca","pera"]
numeros = [1,2,3,4,5,6]
concatenar = frutas + numeros
print(concatenar)

# Exercício 6: Use um loop for para percorrer e imprimir todos os elementos da lista frutas.
frutas = ["uva", "maca", "pera"]
for fruta in frutas:
    print(fruta)

# Exercício 7: Verifique se o número 5 está presente na lista numeros e imprima uma mensagem informando se ele está na lista ou não.

numeros = [1,2,3,4,5]
if 5 in numeros:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")
