from tkinter import *
from tkinter import ttk, messagebox
from cache_musicos import Cache
from producao import Producao
from som import Som
from calcula import CalculadorCache
from opcoes import Opcoes

configurar = Opcoes()

def calculate():
    try:
        trampo1_musicos = Cache(quantidade_musicos.get(),
            float(cache_musicos.get()), float(distancia_musicos.get()), configurar)

        trampo1_producao = Producao(nota.get(),
            venda.get(), producao.get())

        trampo1_som = Som(pa_quantidade.get(), 
            retorno_quantidade.get(), mic.get(), cabos.get(), 
            float(km_som.get()), tecnico_quantidade.get(), configurar)

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

def gerar_label(texto, coluna, linha):
    ttk.Label(mainframe, text=texto).grid(
    column=coluna, row=linha, sticky=W)

# parte dos musicos:
gerar_label("VALORES REFERENTES À BANDA", 1, 1)
gerar_label("Quantidade de músicos:", 1, 2)
quantidade_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=quantidade_musicos).grid(
    column=2, row=2, sticky=(W, E))
gerar_label("Cachê de cada músico:", 1, 3)
cache_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=cache_musicos).grid(
    column=2, row=3, sticky=(W, E))
gerar_label("Distancia total:", 1, 4)
distancia_musicos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=distancia_musicos).grid(
    column=2, row=4, sticky=(W, E))

# parte da produção:
gerar_label("VALORES REFERENTES À PRODUÇÃO", 1, 5)
gerar_label("Porcentagem Nota Fiscal:", 1, 6)
nota = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=nota).grid(
    column=2, row=6, sticky=(W, E))
gerar_label("Porcentagem Venda:", 1, 7)
venda = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=venda).grid(
    column=2, row=7, sticky=(W, E))
gerar_label("Porcentagem de Produção:", 1, 8)
producao = DoubleVar()
ttk.Entry(mainframe, width=7, textvariable=producao).grid(
    column=2, row=8, sticky=(W, E))

# parte do som:
gerar_label("VALORES REFERENTES À SONORIZAÇÃO", 1, 9)
gerar_label("Quantidade de PAs:", 1, 10)
pa_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=pa_quantidade).grid(
    column=2, row=10, sticky=(W, E))
gerar_label("Quantidade de retornos:", 1, 11)
retorno_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=retorno_quantidade).grid(
    column=2, row=11, sticky=(W, E))
gerar_label("Quantidade de microfones:", 1, 12)
mic = IntVar()
ttk.Entry(mainframe, width=7, textvariable=mic).grid(
    column=2, row=12, sticky=(W, E))
gerar_label("Quantidade de cabos:", 1, 13)
cabos = IntVar()
ttk.Entry(mainframe, width=7, textvariable=cabos).grid(
    column=2, row=13, sticky=(W, E))
gerar_label("Distancia total som:", 1, 14)
km_som = IntVar()
ttk.Entry(mainframe, width=7, textvariable=km_som).grid(
    column=2, row=14, sticky=(W, E))
gerar_label("Quantidade técnicos:", 1, 15)
tecnico_quantidade = IntVar()
ttk.Entry(mainframe, width=7, textvariable=tecnico_quantidade).grid(
    column=2, row=15, sticky=(W, E))

# parte do resultado
gerar_label("RESULTADO:", 1, 16)
ttk.Button(mainframe, text="Calcular", default="active",
    command=calculate).grid(column=2, row=16, sticky=W)

meters = IntVar()
ttk.Label(mainframe, textvariable=meters, foreground="green").grid(
    column=1, row=17, sticky=(W, E))

# parte das configurações:
def new_window():
    def gerar_tabela(texto, coluna, linha):
        ttk.Label(mainframe, text=texto).grid(
        column=coluna, row=linha, sticky=W)
    gerar_tabela("** CONFIGURAÇÕES **", 3,0)
    gerar_tabela("valor PA:", 3,1)
    pa_valor = DoubleVar(value=200.0)
    ttk.Entry(mainframe, width=7, textvariable=pa_valor).grid(
        column=4, row=1, sticky=(W, E))
    gerar_tabela("valor retorno:", 3,2)
    retorno_valor = DoubleVar(value=150.0)
    ttk.Entry(mainframe, width=7, textvariable=retorno_valor).grid(
        column=4, row=2, sticky=(W, E))
    gerar_tabela("valor Mesa de Som:", 3,3)
    mesa_som_valor = DoubleVar(value=150.0)
    ttk.Entry(mainframe, width=7, textvariable=mesa_som_valor).grid(
        column=4, row=3, sticky=(W, E))
    gerar_tabela("valor Microfone: ", 3,4)
    mic_valor = DoubleVar(value=50.0)
    ttk.Entry(mainframe, width=7, textvariable=mic_valor).grid(
        column=4, row=4, sticky=(W, E))
    gerar_tabela("valor Cabo:", 3,5)
    cabo_valor = DoubleVar(value=100.0)
    ttk.Entry(mainframe, width=7, textvariable=cabo_valor).grid(
        column=4, row=5, sticky=(W, E))
    gerar_tabela("valor Técnico:", 3,6)
    tecnico_valor = DoubleVar(value=100.0)
    ttk.Entry(mainframe, width=7, textvariable=tecnico_valor).grid(
        column=4, row=6, sticky=(W, E))
    gerar_tabela("valor Km/Litro:", 3,7)
    km_l_valor = DoubleVar(value=6.0)
    ttk.Entry(mainframe, width=7, textvariable=km_l_valor).grid(
        column=4, row=7, sticky=(W, E))
    gerar_tabela("valor Alimentação:", 3,8)
    alimentacao_valor = DoubleVar(value=0.0)
    ttk.Entry(mainframe, width=7, textvariable=alimentacao_valor).grid(
        column=4, row=8, sticky=(W, E))
    
    def opcoes():
        global configurar
        configurar = Opcoes(valor_pa=pa_valor.get(),
                      valor_retorno=retorno_valor.get(),
                      valor_mesa_som=mesa_som_valor.get(),
                      valor_mic=mic_valor.get(),
                      valor_cabo=cabo_valor.get(),
                      valor_tecnico=tecnico_valor.get(),
                      km_por_litro=km_l_valor.get(),
                      valor_alimentacao=alimentacao_valor.get())
        return configurar

    ttk.Button(mainframe, text="Salvar", command=opcoes,
        default="active").grid(column=4, row=9, sticky=W)

ttk.Button(mainframe, text="Configurações", command=new_window).grid(
    column=2, row=0, sticky=W)

# colocando tudo no lugar:
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=20, pady=5)

root.mainloop()