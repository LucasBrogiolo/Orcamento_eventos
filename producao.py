class Producao:
    def __init__(self, nota, venda, producao):
        self._nota = nota
        self._venda = venda
        self._producao = producao
        self.__total = self.soma_percentual()

    def soma_percentual(self):
        if (self._nota > 1) or (self._venda > 1) or (self._producao > 1):
            raise ValueError("nota precisa estar entre 0.0 e 0.99")
        else:
            total = self._producao + self._venda + self._nota
            return total

    @property
    def total(self):
        return self.__total