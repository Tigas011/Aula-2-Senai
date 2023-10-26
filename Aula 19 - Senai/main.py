# **Exercício 1 PROJETOS:**

# O seu chefe pediu para que você criasse um planejamento para a criação de um relógio digital que 

# todas a equipe usaria.

# Alinhe as etapas de desenvolvimento. 

# Envie por e-mail.

# **Exercício 1: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto "Olá, Tkinter!" no centro da janela.

# **Exercício 2: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto seu nome no centro da janela

# [Resolução](https://www.notion.so/Resolu-o-003c9d2370274d6793b1952c7a2025e4?pvs=21)


import tkinter as tk

# Função para criar uma janela com um texto centralizado
def criar_janela(texto):
    # Criar uma instância da classe Tk
    janela = tk.Tk()
    
    # Definir o título da janela
    janela.title("Relógio Digital")
    
    # Obter as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Definir as dimensões da janela
    largura_janela = 200
    altura_janela = 100
    
    # Calcular a posição para centralizar a janela na tela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2
    
    # Definir as dimensões e a posição da janela
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    
    # Criar um rótulo com o texto centralizado
    label = tk.Label(janela, text=texto, font=("Arial", 16))
    label.pack(expand=True)
    
    # Iniciar o loop principal da aplicação
    janela.mainloop()

# Exercício 1: Criar uma janela com o texto "Olá, Tkinter!" centralizado
texto_exercicio1 = "Olá, Tkinter!"
criar_janela(texto_exercicio1)

# Exercício 2: Criar uma janela com o seu nome centralizado
texto_exercicio2 = "Seu Nome"
criar_janela(texto_exercicio2)
