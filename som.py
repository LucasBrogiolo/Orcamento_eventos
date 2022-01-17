from opcoes import Opcoes

class Som:
    def __init__(self, pa, retorno, microfones, cabos, km_distancia, tecnico, opcoes):
        self._pa = pa
        self._retorno = retorno
        self._microfones = microfones
        self._cabos = cabos
        self._km_distancia = km_distancia
        self._tecnico = tecnico
        self._opcoes = opcoes


    def __str__(self):
        return (f"PAs : {self._pa}\nRetornos: {self._retorno}\n"
                f"Microfones: {self._microfones}\nCabos: {self._cabos}\n"
                f"Distancia: {self._km_distancia}\nTécnicos: {self._tecnico}\n"
                f"Total custo som: {self.total()}")

    def gastos_combustivel(self):
        combustivel = self._km_distancia / self._opcoes.km_por_litro
        if combustivel < 50:
            return 50
        else:
            return combustivel

    def total(self):
        combustivel = self.gastos_combustivel()
        pa = self._pa * self._opcoes.valor_pa
        retorno = self._retorno * self._opcoes.valor_retorno
        cabos = self._cabos * self._opcoes.valor_cabo
        if self._microfones:
            microfones = self._retorno * self._opcoes.valor_retorno
            mesa_som = self._opcoes.valor_mesa_som
        else:
            return 0
        equipe = self._tecnico * self._opcoes.valor_tecnico
        resultado = combustivel + pa + retorno + cabos + microfones + equipe + mesa_som
        return resultado