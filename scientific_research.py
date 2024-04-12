import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def plot_grafico():
    # Desativa temporariamente a interface principal
    root.attributes('-disabled', True)

    # Cria uma nova janela para o gráfico
    grafico_window = tk.Toplevel(root)
    grafico_window.title('Gráfico')

    # Cria um gráfico simples
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title('Exemplo de Gráfico')

    # Adiciona o gráfico à nova janela
    canvas = FigureCanvasTkAgg(fig, master=grafico_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Adiciona a barra de ferramentas de navegação
    toolbar = NavigationToolbar2Tk(canvas, grafico_window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Função para reativar a interface principal quando a janela do gráfico for fechada
    def reativar_interface_principal():
        root.attributes('-disabled', False)
        grafico_window.destroy()

    # Configura a ação para quando a janela do gráfico for fechada
    grafico_window.protocol("WM_DELETE_WINDOW", reativar_interface_principal)

    # Espera até que a janela do gráfico seja fechada
    grafico_window.wait_window()

# Cria a janela principal
root = tk.Tk()

# Botão para plotar o gráfico
btn_plotar = ttk.Button(root, text='Plotar Gráfico', command=plot_grafico)
btn_plotar.pack()

# Executa o loop principal da aplicação
root.mainloop()
