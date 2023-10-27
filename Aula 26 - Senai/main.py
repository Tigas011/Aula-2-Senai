import tkinter as tk
from PIL import Image, ImageTk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertendo altura de cm para m
        imc = peso / (altura ** 2)
        resultado.config(text=f"Seu IMC é {imc:.2f}")

        # Exibindo a imagem correspondente ao IMC
        if imc < 18.5:
            imagem = Image.open("assets/abaixo_peso.png")
        elif imc < 24.9:
            imagem = Image.open("assets/normal.png")
        elif imc < 29.9:
            imagem = Image.open("assets/sobrepeso.png")
        else:
            imagem = Image.open("assets/obesidade.png")

        # Redimensionando a imagem com antialiasing usando o método thumbnail
        imagem.thumbnail((100, 100))

        foto = ImageTk.PhotoImage(imagem)
        foto_label.config(image=foto)
        foto_label.image = foto
    except ValueError:
        resultado.config(text="Por favor, insira valores válidos.")

# Restante do código permanece o mesmo...


# Restante do código permanece o mesmo...


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Criando os widgets
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.grid(row=0, column=0)

entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1)

label_altura = tk.Label(root, text="Altura (cm):")
label_altura.grid(row=1, column=0)

entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1)

calcular_button = tk.Button(root, text="Calcular IMC", command=calcular_imc)
calcular_button.grid(row=2, column=0, columnspan=2)

resultado = tk.Label(root, text="")
resultado.grid(row=3, column=0, columnspan=2)

foto_label = tk.Label(root)
foto_label.grid(row=0, column=2, rowspan=4)

# Iniciando o loop principal da aplicação
root.mainloop()


