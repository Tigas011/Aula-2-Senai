# ESTILOS DENTRO DA TKINTER

# A decisão de usar `import tkinter as tk` em vez de `from tkinter import *` é uma questão de boas práticas de programação e pode depender do contexto do seu código.
# Ambas as abordagens têm vantagens e desvantagens.

# Usar `import tkinter as tk` é geralmente considerado uma prática mais segura e recomendada por várias razões:

# 1. Evita Conflitos de Nomes:** Quando você importa todo o módulo com `import tkinter as tk`, você cria um alias (apelido) para o módulo que é `tk`. 
# Isso evita conflitos de nomes entre os objetos do módulo Tkinter e outros objetos que você pode estar usando em seu programa. Se você usar `from tkinter import *`, 
# todos os nomes do módulo Tkinter serão importados diretamente no espaço de nomes atual, o que pode causar conflitos de nomes.

# 2. Legibilidade do Código:** Quando você lê o código, é mais claro saber que objetos pertencem ao módulo Tkinter, pois você sempre os acessa usando `tk.<nome_do_objeto>`. 
# Isso torna o código mais legível e facilita a identificação das origens dos objetos.

# 3. Melhor Prática para Grandes Projetos: Em projetos maiores e mais complexos, é comum evitar a importação de todos os nomes
# diretamente no espaço de nomes global, pois isso pode tornar o código mais difícil de entender e depurar.
# No entanto, a abordagem `from tkinter import *` pode ser conveniente para scripts pequenos ou em situações específicas, onde você tem certeza de que não haverá conflitos de nomes. 
# Ela economiza digitação, pois você pode acessar os objetos do módulo diretamente, sem a necessidade de prefixar com `tk.`.
# Em resumo, a escolha entre `import tkinter as tk` e `from tkinter import *` depende do contexto do seu projeto, do tamanho do código e das considerações de clareza e segurança.
# Para projetos maiores e mais organizados, a abordagem `import tkinter as tk` é geralmente preferida.

# MANIPULANDO API’S

# O QUE É UMA API:

# Uma API (Interface de Programação de Aplicativos) é um conjunto de regras e protocolos que permite que diferentes softwares se comuniquem uns com os outros. 
# Ela define as maneiras pelas quais componentes de software devem interagir, tornando possível a integração de diferentes sistemas e aplicativos.
# As APIs são usadas para solicitar e fornecer dados ou funcionalidades entre aplicativos.

# Aqui estão alguns pontos-chave relacionados a APIs:

# 1. Comunicação entre Aplicativos:** As APIs permitem que um aplicativo faça solicitações a outro aplicativo, solicitando dados, funcionalidades ou serviços específicos.
# Isso é fundamental para a integração de sistemas e a automação de tarefas.

# 2. Padrões e Protocolos:** As APIs geralmente seguem padrões e protocolos bem definidos, como HTTP (para APIs da web), SOAP, REST, GraphQL, etc.
# Esses padrões facilitam a comunicação entre diferentes aplicativos, independentemente das linguagens de programação que estão sendo usadas.


# 3. Endpoints: As APIs geralmente fornecem endpoints, que são URLs específicos que você pode acessar para realizar operações específicas.
# Por exemplo, uma API da web pode ter endpoints para buscar informações, criar registros, atualizar dados, etc.

# 4. Autenticação e Autorização: Muitas APIs requerem autenticação para garantir que apenas usuários autorizados tenham acesso a determinados recursos.
# Isso é feito por meio de chaves de API, tokens de acesso, ou outros mecanismos de autenticação.

# 5. Formato de Dados: As APIs normalmente respondem em um formato de dados específico, como JSON ou XML.
# Esses formatos tornam os dados fáceis de serem consumidos e processados por aplicativos.

# 6. Uso Comum de APIs: APIs são usadas em uma ampla variedade de cenários, como redes sociais (por exemplo, a API do Twitter),
# serviços de pagamento (por exemplo, a API do PayPal), serviços de mapas (por exemplo, a API do Google Maps), e muitos outros.

# 7. Desenvolvimento de Aplicativos: Desenvolvedores de software usam APIs para incorporar funcionalidades de terceiros em seus próprios aplicativos, o que economiza tempo e recursos.

# 8. Documentação: A maioria das APIs é acompanhada por documentação detalhada que descreve como usar a API, quais endpoints estão disponíveis e como autenticar as solicitações.

# Se você deseja usar uma API, geralmente começa consultando a documentação da API para entender como usá-la e, em seguida, faz solicitações apropriadas usando a linguagem de programação de sua escolha. 
# A resposta da API é processada para obter os dados ou funcionalidades desejados.
# Lembre-se de que, ao usar APIs, você deve respeitar os termos de uso e as políticas de autenticação e autorização definidos pela API específica que está sendo usada.

# import tkinter as tk
# import requests

# def search_pokemon():
#     pokemon_name = entry.get()
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
#     if response.status_code == 200:
#         data = response.json()
#         result_label.config(text=f"Nome: {data['name'].capitalize()}\n"
#                                  f"Altura: {data['height']}\n"
#                                  f"Peso: {data['weight']}")
#     else:
#         result_label.config(text="Pokémon não encontrado.")

# # Criação da janela
# window = tk.Tk()
# window.title("Informações de Pokémon")

# # Caixa de entrada
# entry = tk.Entry(window, width=35)
# entry.pack(pady=10)

# # Botão de pesquisa
# search_button = tk.Button(window, text="Buscar", command=search_pokemon, font= 'arial', fg='blue', width=15 )
# search_button.pack()

# # Rótulo para exibir os resultados
# result_label = tk.Label(window, text="", width=150, font='arial', fg='green', height=35 )
# result_label.pack()

# # Inicia a janela
# window.mainloop()



# if response.status_code == 200:: Este é um condicional que verifica se o código de status da resposta 
# da API é igual a 200. O código de status 200 é geralmente usado para indicar que a solicitação foi bem-sucedida.

# import requests
# import tkinter as tk


# def get_lyrics():
#     artist = artist_entry.get()
#     song = song_entry.get()
#     api_url = f"https://api.vagalume.com.br/search.php?art={artist}&mus={song}"
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         data = response.json()
#         lyrics = data['mus'][0]['text']
#         display_lyrics(lyrics)
#     else:
#         result_label.config(text="Letra não encontrada")

# def display_lyrics(lyrics):
#     result_text.delete(1.0, "end")  # Limpa o conteúdo anterior
#     result_text.insert(tk.END, lyrics)

# app = tk.Tk()
# app.title("Busca de Letras de Músicas")

# artist_label = tk.Label(app, text="Artista:")
# artist_label.pack()

# artist_entry = tk.Entry(app)
# artist_entry.pack()

# song_label = tk.Label(app, text="Música:")
# song_label.pack()

# song_entry = tk.Entry(app)
# song_entry.pack()

# search_button = tk.Button(app, text="Buscar Letra", command=get_lyrics)
# search_button.pack()

# result_text = tk.Text(app, height=10, width=60)
# result_text.pack()

# result_label = tk.Label(app, text="")
# result_label.pack()

# app.mainloop()

