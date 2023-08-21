import tkinter as tk
from tkinter import messagebox

def fazer_pedido():
    resposta = messagebox.askyesno("Pedido", "Variável da pergunta")
    if resposta:
        messagebox.showinfo("Resposta", "Variável da resposta positiva.")
    else:
        messagebox.showinfo("Resposta", "Variável da resposta negativa.")

# Criando a janela
janela = tk.Tk()
janela.title("Variável do nome da janela")

# Criando um botão para fazer o pedido
botao_pedido = tk.Button(janela, text="Fazer Pedido", command=fazer_pedido)
botao_pedido.pack(padx=20, pady=20)

# Iniciando o loop principal da interface gráfica
janela.mainloop()
