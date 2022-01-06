class Som:
    def __init__(self, pa, retorno, microfones, cabos, km_distancia, tecnico=0):
        self.pa = pa
        self.retorno = retorno
        self.microfones = microfones
        self.cabos = cabos
        self.km_distancia = km_distancia
        self.tecnico = tecnico
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
        pa = self.pa * 200
        retorno = self.retorno * 150
        if self.microfones:
            microfones = self.retorno * 50
            mesa_som = 150
        else:
            return 0
        equipe = self.tecnico * 100
        total = combustivel + pa + retorno + microfones + equipe + mesa_som
        return total