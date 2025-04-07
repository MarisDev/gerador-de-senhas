import string
import random
import tkinter as tk
from tkinter import ttk
import pyperclip

def gerar_senha(tamanho):
    caracteres = ""

    if usar_maiusculas.get():
        caracteres += string.ascii_uppercase
    if usar_minusculas.get():
        caracteres += string.ascii_lowercase
    if usar_numeros.get():
        caracteres += string.digits
    if usar_simbolos.get():
        caracteres += string.punctuation

    if not caracteres:
        return "Selecione pelo menos uma opção"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_e_exibir_senha():
    try:
        tamanho = int(spinbox_tamanho.get())
        senha = gerar_senha(tamanho)
        entrada_senha.delete(0, tk.END)
        entrada_senha.insert(0, senha)
    except ValueError:
        entrada_senha.delete(0, tk.END)
        entrada_senha.insert(0, "Erro: valor inválido")

def copiar_senha():
    senha = entrada_senha.get()
    if senha and "Erro" not in senha and "Selecione" not in senha:
        pyperclip.copy(senha)

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x350")
janela.configure(bg="#2C3E50")

usar_maiusculas = tk.BooleanVar(value=True)
usar_minusculas = tk.BooleanVar(value=True)
usar_numeros = tk.BooleanVar(value=True)
usar_simbolos = tk.BooleanVar(value=True)

style = ttk.Style()
style.configure("TLabel", font=("Ariel", 12), background="#2C3E50", foreground="white")
style.configure("TButton", font=("Arial", 12), padding=6)

label_titulo = ttk.Label(janela, text="Gerador de Senhas Seguras", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

frame = ttk.Frame(janela)
frame.pack(pady=10)

ttk.Label(frame, text="Tamanho da senha:").grid(row=0, column=0, padx=5)
spinbox_tamanho = ttk.Spinbox(frame, from_=6, to=32, width=5)
spinbox_tamanho.set(12)
spinbox_tamanho.grid(row=0, column=1)

frame_checks = ttk.Frame(janela)
frame_checks.pack(pady=10)

ttk.Checkbutton(frame_checks, text="Letras maiúsculas", variable=usar_maiusculas).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(frame_checks, text="Letras minúsculas", variable=usar_minusculas).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(frame_checks, text="Números", variable=usar_numeros).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame_checks, text="Símbolos", variable=usar_simbolos).grid(row=3, column=0, sticky="w")

ttk.Button(janela, text="Gerar Senha", command=gerar_e_exibir_senha).pack(pady=5)

entrada_senha = ttk.Entry(janela, font=("Arial", 14), justify="center", width=30)
entrada_senha.pack(pady=5)

ttk.Button(janela, text="Copiar Senha", command=copiar_senha).pack(pady=5)

janela.mainloop()
