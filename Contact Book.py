import tkinter as tk

def adicionar_contato():
    name = nome_entry.get()
    phone_number = telefone_entry.get()
    names.append(name)
    phone_numbers.append(phone_number)
    atualizar_lista()

def pesquisar_contato():
    search_term = pesquisa_entry.get()
    resultado_text.delete(1.0, tk.END)
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        resultado_text.insert(tk.END, f"Nome: {search_term}\nNúmero de telefone: {phone_number}")
    else:
        resultado_text.insert(tk.END, "Nome não encontrado")

def atualizar_lista():
    lista_contatos.delete(0, tk.END)
    for name, phone_number in zip(names, phone_numbers):
        lista_contatos.insert(tk.END, f"{name}: {phone_number}")

janela = tk.Tk()
janela.title("Gerenciador de Contatos")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Telefone:").grid(row=1, column=0, padx=10, pady=5)
telefone_entry = tk.Entry(janela)
telefone_entry.grid(row=1, column=1, padx=10, pady=5)

adicionar_button = tk.Button(janela, text="Adicionar Contato", command=adicionar_contato)
adicionar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

lista_contatos = tk.Listbox(janela, width=40)
lista_contatos.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

tk.Label(janela, text="Pesquisar por nome:").grid(row=4, column=0, padx=10, pady=5)
pesquisa_entry = tk.Entry(janela)
pesquisa_entry.grid(row=4, column=1, padx=10, pady=5)

pesquisar_button = tk.Button(janela, text="Pesquisar", command=pesquisar_contato)
pesquisar_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

resultado_text = tk.Text(janela, height=5, width=40)
resultado_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

names = []
phone_numbers = []

janela.mainloop()
