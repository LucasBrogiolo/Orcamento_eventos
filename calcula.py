class CalculadorCache:
    def calcula(self, cache, producao, som):
        if som == 0:
            resultado = (cache.total) / (1-producao.total)
            return (f"Orçamento Total: R$ {resultado:.2f}\n"
                    f"Custo musicos: R$ {cache.total:.2f}\n"
                    f"Custo som: R$ 00.00\n"
                    f"Custo produção: R$ {(producao.total*resultado):.2f}")

        else:
            resultado = (cache.total + som.total) / (1-producao.total)
            return (f"Orçamento Total: R$ {resultado:.2f}\n"
                    f"Custo musicos: R$ {cache.total:.2f}\n"
                    f"Custo som: R$ {som.total:.2f}\n"
                    f"Custo produção: R$ {(producao.total*resultado):.2f}")

# if __name__ == "__main__":
#     from cache_musicos import Cache
#     from producao import Producao
#     from som import Som

#     trampo1_musicos = Cache(4, 220, 80)
#     trampo1_producao = Producao(0.0, 0.2, 0.2)
#     trampo1_som = Som(0, 0, 0, 0, 0)
#     total = CalculadorCache()
#     resultado = total.calcula(trampo1_musicos, trampo1_producao, 0)
#     print(resultado)