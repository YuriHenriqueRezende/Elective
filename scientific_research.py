import tkinter as tk

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Principal")
        self.geometry("300x200")

        self.botao_abrir = tk.Button(self, text="Abrir Nova Janela", command=self.abrir_nova_janela)
        self.botao_abrir.pack(pady=20)

    def abrir_nova_janela(self):
        self.withdraw()  # Esconde a janela principal
        self.nova_janela = JanelaSecundaria(self)
        self.nova_janela.protocol("WM_DELETE_WINDOW", self.fechar_nova_janela)

    def fechar_nova_janela(self):
        self.nova_janela.destroy()
        self.deiconify()  # Mostra a janela principal

class JanelaSecundaria(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Nova Janela")
        self.geometry("200x100")
        self.label = tk.Label(self, text="Esta é uma nova janela")
        self.label.pack(padx=10, pady=10)

        self.botao_voltar = tk.Button(self, text="Voltar", command=self.voltar_para_janela_principal)
        self.botao_voltar.pack(pady=10)

    def voltar_para_janela_principal(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()
