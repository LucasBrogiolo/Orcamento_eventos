from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cache_musicos import Cache
from producao import Producao
from som import Som
from calcula import CalculadorCache


def calculate(*args):
    try:
        trampo1_musicos = Cache(
            qt_musicos_entry.get(),
            float(cache_entry.get()),
            float(distancia_musicos_entry.get()))
        trampo1_producao = Producao(
            float(nota_entry.get()),
            float(venda_entry.get()),
            float(producao_entry.get()))
        trampo1_som = Som(
            pa_entry.get(),
            retorno_entry.get(),
            mic_entry.get(),
            cabos_entry.get(),
            float(km_som_entry.get()),
            tecnico_entry.get())
        total = CalculadorCache()
        resultado = total.calcula(
            trampo1_musicos,
            trampo1_producao,
            trampo1_som
            )
        meters.set(resultado)
    except:
        messagebox.showerror("Alert", "Insira valores válidos")
        
root = Tk()
root.title("Cálculo do Orçamento")

mainframe = ttk.Frame(root, padding="3 30 3 30")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

quantidade_musicos = IntVar()
qt_musicos_entry = ttk.Entry(mainframe, width=7, textvariable=quantidade_musicos)
qt_musicos_entry.grid(column=2, row=2, sticky=(W, E))

cache_musicos = IntVar()
cache_entry = ttk.Entry(mainframe, width=7, textvariable=cache_musicos)
cache_entry.grid(column=2, row=3, sticky=(W, E))

distancia_musicos = IntVar()
distancia_musicos_entry = ttk.Entry(mainframe, width=7, textvariable=distancia_musicos)
distancia_musicos_entry.grid(column=2, row=4, sticky=(W, E))

nota = IntVar()
nota_entry = ttk.Entry(mainframe, width=7, textvariable=nota)
nota_entry.grid(column=2, row=6, sticky=(W, E))

venda = IntVar()
venda_entry = ttk.Entry(mainframe, width=7, textvariable=venda)
venda_entry.grid(column=2, row=7, sticky=(W, E))

producao = IntVar()
producao_entry = ttk.Entry(mainframe, width=7, textvariable=producao)
producao_entry.grid(column=2, row=8, sticky=(W, E))

pa_quantidade = IntVar()
pa_entry = ttk.Entry(mainframe, width=7, textvariable=pa_quantidade)
pa_entry.grid(column=2, row=10, sticky=(W, E))

retorno_quantidade = IntVar()
retorno_entry = ttk.Entry(mainframe, width=7, textvariable=retorno_quantidade)
retorno_entry.grid(column=2, row=11, sticky=(W, E))

mic = IntVar()
mic_entry = ttk.Entry(mainframe, width=7, textvariable=mic)
mic_entry.grid(column=2, row=12, sticky=(W, E))

cabos = IntVar()
cabos_entry = ttk.Entry(mainframe, width=7, textvariable=cabos)
cabos_entry.grid(column=2, row=13, sticky=(W, E))

km_som = IntVar()
km_som_entry = ttk.Entry(mainframe, width=7, textvariable=km_som)
km_som_entry.grid(column=2, row=14, sticky=(W, E))

tecnico_quantidade = IntVar()
tecnico_entry = ttk.Entry(mainframe, width=7, textvariable=tecnico_quantidade)
tecnico_entry.grid(column=2, row=15, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=2, row=16, sticky=W)

ttk.Label(mainframe, text="VALORES REFERENTES À BANDA").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Quantidade de músicos:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Cachê de cada músico:").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Distancia total:").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="VALORES REFERENTES À PRODUÇÃO").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Porcentagem Nota Fiscal:").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Porcentagem Venda:").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Porcentagem de Produção:").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="VALORES REFERENTES À SONORIZAÇÃO").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="Quantidade de PAs:").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, text="Quantidade de retornos:").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, text="Quantidade de microfones:").grid(column=1, row=12, sticky=W)
ttk.Label(mainframe, text="Quantidade de cabos:").grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, text="Distancia total som:").grid(column=1, row=14, sticky=W)
ttk.Label(mainframe, text="Quantidade técnicos:").grid(column=1, row=15, sticky=W)
ttk.Label(mainframe, text="RESULTADO:").grid(column=1, row=16, sticky=W)

meters = IntVar()
ttk.Label(mainframe, textvariable=meters).grid(column=1, row=17, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=20, pady=5)

root.mainloop()