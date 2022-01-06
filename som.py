class Som:
    def __init__(self, pa, retorno, microfones, cabos, km_distancia, tecnico=0):
        self._pa = pa
        self._retorno = retorno
        self._microfones = microfones
        self._cabos = cabos
        self._km_distancia = km_distancia
        self._tecnico = tecnico
        self.__total = self.calculo_total()

    @property
    def total(self):
        return self.__total

    def gastos_combustivel(self):
        combustivel = self.km_distancia / 6
        if combustivel < 50:
            return 50
        else:
            return combustivel

    def calculo_total(self):
        combustivel = self.gastos_combustivel()
        pa = self._pa * 200
        retorno = self._retorno * 150
        if self._microfones:
            microfones = self._retorno * 50
            mesa_som = 150
        else:
            return 0
        equipe = self._tecnico * 100
        total = combustivel + pa + retorno + microfones + equipe + mesa_som
        return total