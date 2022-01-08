from tkinter import *
from tkinter import ttk, messagebox
from cache_musicos import Cache
from producao import Producao
from som import Som
from calcula import CalculadorCache


def calculate():
    try:
        trampo1_musicos = Cache(quantidade_musicos.get(),
            float(cache_musicos.get()), float(distancia_musicos.get()))

        trampo1_producao = Producao(nota.get(),
            venda.get(), producao.get())

        trampo1_som = Som(pa_quantidade.get(), 
            retorno_quantidade.get(), mic.get(), cabos.get(), 
            float(km_som.get()), tecnico_quantidade.get())

        total = CalculadorCache()

        resultado = total.calcula(trampo1_musicos,
            trampo1_producao, trampo1_som)

        meters.set(resultado)
    except:
        messagebox.showerror("Alert", "Insira valores válidos")

root = Tk()
root.title("*** Cálculo do Orçamento ***")

mainframe = ttk.Frame(root, padding="3 30 3 50")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# parte dos musicos:
quantidade_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=quantidade_musicos).grid(
    column=2, row=2, sticky=(W, E))

cache_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=cache_musicos).grid(
    column=2, row=3, sticky=(W, E))

distancia_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=distancia_musicos).grid(
    column=2, row=4, sticky=(W, E))

# parte da produção:
nota = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=nota).grid(
    column=2, row=6, sticky=(W, E))

venda = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=venda).grid(
    column=2, row=7, sticky=(W, E))

producao = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=producao).grid(
    column=2, row=8, sticky=(W, E))

# parte do som:
pa_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=pa_quantidade).grid(
    column=2, row=10, sticky=(W, E))

retorno_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=retorno_quantidade).grid(
    column=2, row=11, sticky=(W, E))

mic = IntVar()
ttk.Entry(mainframe, width=7, textvariable=mic).grid(
    column=2, row=12, sticky=(W, E))

cabos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=cabos).grid(
    column=2, row=13, sticky=(W, E))

km_som = IntVar()
ttk.Entry(mainframe, width=7, textvariable=km_som).grid(
    column=2, row=14, sticky=(W, E))

tecnico_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=tecnico_quantidade).grid(
    column=2, row=15, sticky=(W, E))

ttk.Button(
    mainframe, text="Calcular", default="active",
    command=calculate).grid(column=2, row=16, sticky=W)

ttk.Label(mainframe, text="VALORES REFERENTES À BANDA").grid(
    column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Quantidade de músicos:").grid(
    column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Cachê de cada músico:").grid(
    column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Distancia total:").grid(
    column=1, row=4, sticky=W)

ttk.Label(mainframe, text="VALORES REFERENTES À PRODUÇÃO").grid(
    column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Porcentagem Nota Fiscal:").grid(
    column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Porcentagem Venda:").grid(
    column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Porcentagem de Produção:").grid(
    column=1, row=8, sticky=W)

ttk.Label(mainframe, text="VALORES REFERENTES À SONORIZAÇÃO").grid(
    column=1, row=9, sticky=W)
ttk.Label(mainframe, text="Quantidade de PAs:").grid(
    column=1, row=10, sticky=W)
ttk.Label(mainframe, text="Quantidade de retornos:").grid(
    column=1, row=11, sticky=W)
ttk.Label(mainframe, text="Quantidade de microfones:").grid(
    column=1, row=12, sticky=W)
ttk.Label(mainframe, text="Quantidade de cabos:").grid(
    column=1, row=13, sticky=W)
ttk.Label(mainframe, text="Distancia total som:").grid(
    column=1, row=14, sticky=W)
ttk.Label(mainframe, text="Quantidade técnicos:").grid(
    column=1, row=15, sticky=W)

ttk.Label(mainframe, text="RESULTADO:").grid(
    column=1, row=16, sticky=W)

meters = IntVar()
ttk.Label(mainframe, textvariable=meters, foreground="green").grid(
    column=1, row=17, sticky=(W, E))

ttk.Button(
    mainframe, text="Configurações").grid(
        column=2, row=0, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=20, pady=5)

root.mainloop()