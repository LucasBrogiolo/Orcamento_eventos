class CalculadorCache:
    def calcula(self, cache, producao, som):
        if som == 0:
            resultado = (cache.total()) / (1-producao.total())
            return (f"Orçamento Total: R$ {resultado:.2f}\n"
                    f"Custo musicos: R$ {cache.total():.2f}\n"
                    f"Custo som: R$ 00.00\n"
                    f"Custo produção: R$ {(producao.total()*resultado):.2f}")

        else:
            resultado = (cache.total() + som.total()) / (1-producao.total())
            return (f"Orçamento Total: R$ {resultado:.2f}\n"
                    f"Custo musicos: R$ {cache.total():.2f}\n"
                    f"Custo som: R$ {som.total():.2f}\n"
                    f"Custo produção: R$ {(producao.total()*resultado):.2f}")