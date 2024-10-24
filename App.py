import tkinter as tk
from tkinter import messagebox

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários")

        self.lista_funcionarios = []

        self.form_frame = tk.Frame(root)
        self.form_frame.pack(padx=10, pady=10)

        #Nome
        self.label_nome = tk.Label(self.form_frame, text="Nome do Funcionário:")
        self.label_nome.grid(row=0, column=0, sticky=tk.W)
        self.entry_nome = tk.Entry(self.form_frame)
        self.entry_nome.grid(row=0, column=1)

        # Recebimento
        self.label_data_recebimento = tk.Label(self.form_frame, text="Dia de Recebimento:")
        self.label_data_recebimento.grid(row=1, column=0, sticky=tk.W)
        self.entry_data_recebimento = tk.Entry(self.form_frame)
        self.entry_data_recebimento.grid(row=1, column=1)

        # Salário
        self.label_salario = tk.Label(self.form_frame, text="Valor do Salário:")
        self.label_salario.grid(row=2, column=0, sticky=tk.W)
        self.entry_salario = tk.Entry(self.form_frame)
        self.entry_salario.grid(row=2, column=1)

        # botão_cadastrar
        self.btn_cadastrar = tk.Button(self.form_frame, text="Cadastrar Funcionário", command=self.cadastrar_funcionario)
        self.btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

        # lista_de_funcionários
        self.lista_frame = tk.Frame(root)
        self.lista_frame.pack(padx=10, pady=10)

        self.label_lista = tk.Label(self.lista_frame, text="Lista de Funcionários:")
        self.label_lista.pack(anchor=tk.W)

        self.lista_box = tk.Listbox(self.lista_frame, width=50)
        self.lista_box.pack()

    def cadastrar_funcionario(self):
        # Obtém os valores dos campos de entrada
        nome = self.entry_nome.get()
        data_recebimento = self.entry_data_recebimento.get()
        salario_funcionario = self.entry_salario.get()

        # Verifica se todos os campos foram preenchidos
        if nome and data_recebimento and salario_funcionario:
            funcionario = f"Nome: {nome}, Dia de Recebimento: {data_recebimento}, Salário: {salario_funcionario}"
            self.lista_funcionarios.append(funcionario)
            self.lista_box.insert(tk.END, funcionario)

            # Limpa os campos de entrada
            self.entry_nome.delete(0, tk.END)
            self.entry_data_recebimento.delete(0, tk.END)
            self.entry_salario.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
