# dicionario = {"key": "value", "key2": "value2"}

# menino = {"nome": "caio", "idade": "18", "endereco": "Rua 30"}
# x = menino["nome"]
# y = menino["idade"]
# z = menino["endereco"]
# print(x)
# print(y)
# print(z)

# menino = {"nome": "caio", "idade": "18", "endereco":True}

# del menino["endereco"]
# print(menino)

# n = menino.pop('idade')
# print(menino)

# menino['notas'] = 7
# # print(menino)

# if 'nome' in menino:
#     print("O nome do menino é", menino['nome'])

# notas ={
# "Jose": 9,
# "Maria":10,
# "Felipe":7
# }

# while c <=10:
# nome = input("Digite o nome do aluno >> ")
# nota = float(input("Digite a nota do aluno >> "))

# if notas.get(nome):
#     print("Já existe o aluno", nome)
# else:
#     notas[nome] = nota
#     print(notas)

#Crie um dicionário que represente um 
#dicionário de sinônimos. Em seguida, 
#peça ao usuário para digitar uma palavra e, 
#se a palavra estiver no dicionário, 
#mostre o seu sinônimo.

#crie um dicionário com 5 letras, e acesse 
#o 3º indice

sinonimos = {
    "feliz": "radiante",
    "triste": "desolado",
    "grande": "colossal",
    "pequeno": "minúsculo",
    "rápido": "veloz"
}

while True:
    palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

    if palavra == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    
    encontrado = False
    
    # Busca nas chaves do dicionário
    for chave in sinonimos:
        if palavra == chave:
            print("Sinônimo de", palavra, "é", sinonimos[chave])
            encontrado = True
            break
    
    # Se não foi encontrado nas chaves, busca nos valores do dicionário
    if not encontrado:
        for chave, valor in sinonimos.items():
            if palavra == valor:
                print("A palavra", chave, "é um sinônimo de", palavra)
                encontrado = True
                break
    
    # Se não foi encontrado, permite ao usuário adicionar a palavra e o sinônimo
    if not encontrado:
        novo_sinonimo = input(f"A palavra '{palavra}' não foi encontrada. Digite o sinônimo da palavra: ").lower()
        sinonimos[palavra] = novo_sinonimo
        print(f"Palavra '{palavra}' e seu sinônimo '{novo_sinonimo}' foram adicionados ao dicionário.")



# Criar um dicionário com 5 letras e acessar o 3º índice
letras = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e'
}

# Acessar o terceiro índice (índice 2) do dicionário de letras
terceiro_indice = letras[2]
print("Terceiro índice do dicionário de letras é:", terceiro_indice)
