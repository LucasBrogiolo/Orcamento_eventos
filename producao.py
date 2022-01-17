class Producao:
    def __init__(self, nota, venda, producao):
        self._nota = nota
        self._venda = venda
        self._producao = producao

    def total(self):
        if (self._nota > 1) or (self._venda > 1) or (self._producao > 1):
            raise ValueError("O valor da nota é um número entre 0.0 e 0.99")
        else:
            resultado = self._producao + self._venda + self._nota
            return resultado