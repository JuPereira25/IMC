import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        resultado = f"Seu IMC é: {imc:.2f}\n"

        if imc < 18.5:
            resultado += "Classificação: Abaixo do peso"
        elif imc < 25:
            resultado += "Classificação: Peso normal"
        elif imc < 30:
            resultado += "Classificação: Sobrepeso"
        else:
            resultado += "Classificação: Obesidade"

        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("350x200")  

# widgets
tk.Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=30, pady=30)
entrada_peso = tk.Entry(janela)
entrada_peso.grid(row=0, column=1)

tk.Label(janela, text="Altura (m):").grid(row=1, column=0, padx=15, pady=15)
entrada_altura = tk.Entry(janela)
entrada_altura.grid(row=1, column=1)

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=2, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=3, columnspan=2, pady=10)

# Executar 
janela.mainloop()
