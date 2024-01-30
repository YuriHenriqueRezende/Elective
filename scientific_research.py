import tkinter as tk

class AnimacaoTextoTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Animação de Texto Tkinter")

        # Configurações da janela
        self.largura = 400
        self.altura = 200
        self.canvas = tk.Canvas(root, width=self.largura, height=self.altura)
        self.canvas.pack()

        # Inicialização da animação
        self.texto = "Olá, Tkinter!"
        self.velocidade = 5
        self.label = self.canvas.create_text(10, self.altura//2, text=self.texto, anchor="w", font=("Arial", 12))

        # Inicia o loop de animação
        self.animar()

    def animar(self):
        # Move o texto horizontalmente
        self.canvas.move(self.label, self.velocidade, 0)

        # Obtém as coordenadas atuais do texto
        posicao = self.canvas.coords(self.label)

        # Verifica se o texto atingiu o meio da janela
        if posicao[0] >= self.largura / 2:
            # Interrompe a animação ao atingir o meio
            return

        # Atualiza a animação após um intervalo de tempo (em milissegundos)
        self.root.after(30, self.animar)

# Cria a janela principal
root = tk.Tk()

# Inicializa a animação
animacao_texto = AnimacaoTextoTkinter(root)

# Inicia o loop principal da interface gráfica
root.mainloop()
