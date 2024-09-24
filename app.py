import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import calendar

# Função para calcular as horas trabalhadas e saldo, considerando o intervalo
def calcular_horas(entrada, saida, entrada_intervalo, saida_intervalo):
    formato = "%H:%M"
    try:
        h_entrada = datetime.strptime(entrada, formato)
        h_saida = datetime.strptime(saida, formato)
        h_entrada_intervalo = datetime.strptime(entrada_intervalo, formato)
        h_saida_intervalo = datetime.strptime(saida_intervalo, formato)
        
        # Calcula o tempo total de trabalho e subtrai o intervalo
        horas_trabalhadas = ((h_saida - h_entrada) - (h_saida_intervalo - h_entrada_intervalo)).total_seconds() / 3600
        jornada_padrao = 8.0
        saldo = horas_trabalhadas - jornada_padrao
        return horas_trabalhadas, saldo
    except ValueError:
        return 0, 0  # Se as horas não forem válidas, retorna 0

# Função para gerar a tabela de dias do mês
def gerar_tabela_mes(mes, ano):
    for widget in frame_tabela.winfo_children():
        widget.destroy()  # Limpa a tabela anterior

    dias_no_mes = calendar.monthrange(ano, mes)[1]  # Obtém o número de dias no mês

    # Cabeçalhos da tabela
    tk.Label(frame_tabela, text="Dia", bg='#3e070a', fg='white').grid(row=0, column=0)
    tk.Label(frame_tabela, text="Entrada (HH:MM)", bg='#3e070a', fg='white').grid(row=0, column=1)
    tk.Label(frame_tabela, text="Entrada Intervalo (HH:MM)", bg='#3e070a', fg='white').grid(row=0, column=2)
    tk.Label(frame_tabela, text="Saída Intervalo (HH:MM)", bg='#3e070a', fg='white').grid(row=0, column=3)
    tk.Label(frame_tabela, text="Saída (HH:MM)", bg='#3e070a', fg='white').grid(row=0, column=4)

    entradas.clear()
    saidas.clear()
    entradas_intervalo.clear()
    saidas_intervalo.clear()

    for dia in range(1, dias_no_mes + 1):
        tk.Label(frame_tabela, text=str(dia), bg='#3e070a', fg='white').grid(row=dia, column=0)  # Exibe o dia

        entrada = tk.Entry(frame_tabela)
        entrada.grid(row=dia, column=1)
        entradas.append(entrada)

        entrada_intervalo = tk.Entry(frame_tabela)
        entrada_intervalo.grid(row=dia, column=2)
        entradas_intervalo.append(entrada_intervalo)

        saida_intervalo = tk.Entry(frame_tabela)
        saida_intervalo.grid(row=dia, column=3)
        saidas_intervalo.append(saida_intervalo)

        saida = tk.Entry(frame_tabela)
        saida.grid(row=dia, column=4)
        saidas.append(saida)

# Função para calcular o total do mês
def calcular_total_mes():
    total_horas = 0
    total_saldo = 0

    for entrada, saida, entrada_intervalo, saida_intervalo in zip(entradas, saidas, entradas_intervalo, saidas_intervalo):
        horas_trabalhadas, saldo = calcular_horas(entrada.get(), saida.get(), entrada_intervalo.get(), saida_intervalo.get())
        total_horas += horas_trabalhadas
        total_saldo += saldo

    if total_saldo < 0:
        messagebox.showinfo('Resultado do Mês', f'O funcionário deve {abs(total_saldo):.2f} horas')
    else:
        messagebox.showinfo('Resultado do Mês', f'A empresa deve {total_saldo:.2f} horas')

# Interface gráfica
root = tk.Tk()
root.title('Banco de Horas - Tabela do Mês com Intervalo')

# Configurações de cores do aplicativo
root.configure(bg='#3e070a')  # Cor de fundo

entradas = []
saidas = []
entradas_intervalo = []
saidas_intervalo = []

# Adicionando logo
logo = tk.PhotoImage(file='C:/Users/Paulo/Desktop/Projetos/Empresas/Dudék/logorest.png')  # Ajuste para o caminho correto da sua imagem
logo = logo.subsample(4, 4)  # Diminuir a imagem para um quarto do tamanho original
logo_label = tk.Label(root, image=logo, bg='#3e070a')
logo_label.grid(row=0, column=0, columnspan=5)  # Ajuste a posição conforme necessário

# Frame para a tabela
frame_tabela = tk.Frame(root, bg='#3e070a')  # Usando a mesma cor para o frame
frame_tabela.grid(row=1, column=0, columnspan=5)

# Gerar tabela automaticamente para o mês atual
mes_atual = datetime.now().month
ano_atual = datetime.now().year
gerar_tabela_mes(mes_atual, ano_atual)

# Botão para calcular o total
tk.Button(root, text='Calcular Total do Mês', command=calcular_total_mes, bg='lightgray', fg='black').grid(row=2, column=0, columnspan=5)

root.mainloop()
