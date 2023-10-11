# cidade = 'São Carlos'
# endereco = 'Rua Cândido Padim, 25 - VIla Prado'
# completo = cidade + endereco
# print(cidade.startswith('Sâo'))
# print(cidade.endswith('Los'))
# print('Rua' in completo)
# print('Avenida' not in completo)

# Texto = "Python é uma linguagem legal"

# print(texto.count('é'))
# print(texto.find('Python',25,50))
# print(texto.rfind('é'))
# print(texto.index('é'))

# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.split('/'))

# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.splitlines())

# f = 'A força eletromotriz induzida em qualquer circuito fechado é igual ao negativo da variação do fluxo magnético com o tempo na área delimitada pelo circuito'
# f1 = f.replace('força','Bicicleta')
# f2 = f.replace('','#')
# print(f1)
# print(f2)

# a = '    Olá mundo    '
# print(f'*{a}*')
# b = a.strip()
# print(f'*{b}*')
# c = a.lstrip()
# print(f'*{c}*')
# d = a.rstrip()
# print(f'*{d}*')

#                                                                     EXERCÍCIO


# Exercício 1: Escreva um programa que verifique se a palavra "python" está presente na string "Estou aprendendo Python".

# frase = "Estou aprendendo Python"

# if "python" in frase.lower():
#     print("A palavra 'python' está presente na string.")
# else:
#     print("A palavra 'python' não está presente na string.")

    
# # exercício 2: Escreva um programa que peça ao usuário para digitar seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).
# nome = input("Digite seu nome: ").lower()

# if nome[0] == 'a':
#     print("Seu nome começa com a letra 'A'.")
# else:
#     print("Seu nome não começa com a letra 'A'.")


# Exercício 3: Escreva um programa que peça ao usuário para digitar uma senha e verifique se a senha contém pelo menos 8 caracteres.

# senha = input("Digite sua senha: ")

# if len(senha) >= 8:
#     print("Senha válida. A senha contém pelo menos 8 caracteres.")
# else:
#     print("Senha inválida. A senha deve conter pelo menos 8 caracteres.")


# Exercício 4: Escreva um programa que peça ao usuário para digitar um número e verifique se o número é uma representação numérica (não contém letras ou símbolos).

# numero = input("Digite um número: ")
# if numero.isdigit():
#     print("O número digitado é uma representação numérica.")
# else:
#     print("O número digitado não é uma representação numérica.")

# Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

# frase = input("Digite uma frase: ").lower()

# count = frase.count("a")
# print(f'A letra "a" aparece {count} vezes na frase.')

# Exercício 6 - Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings
# possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

str1 = input("Digite uma frase aqui: ")
str2 = input("Digite outra frase: ")
comprimento1 = len(str1)
comprimento2 = len(str2)

print(len(str2), str2)
print(len(str2), str2)

if str1 == str2:
    print("As duas frases tem o mesmo comprimento.")
else:
    print("O comprimento é diferente.") 


# 7 - Faça um programa que solicite o nome do usuário e imprima-o na vertical.




