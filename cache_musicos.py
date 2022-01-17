from opcoes import Opcoes

class Cache:
    def __init__(self, quantidade_musicos, valor_cache, km_total, opcoes):
        self.__quantidade_musicos = quantidade_musicos
        self.__valor_cache = valor_cache
        self.km_total = km_total
        self._opcoes = opcoes

        self.__pedagios = []
        self.__carros = self.numero_carros()


    def __str__(self) -> str:
        return (f"Quantidade de musicos: {self.__quantidade_musicos}\n"
                f"Cache Individual: {self.__valor_cache}\n"
                f"Distancia a percorrer: {self.km_total}km\n"
                f"Valor alimentacao individual: {self._opcoes.valor_alimentacao}\n"
                f"Pedágios: {self.__pedagios}\n"
                f"Quantidade de Carros: {self.__carros}")

    @property
    def quantidade_musicos(self):
        return self.__quantidade_musicos

    @quantidade_musicos.setter
    def quantidade_musicos(self, valor):
        self.__quantidade_musicos = valor

    @property
    def valor_cache(self):
        return self.__valor_cache

    @valor_cache.setter
    def valor_cache(self, valor):
        self.__valor_cache = valor

    @property
    def carros(self):
        return self.__carros

    @property
    def pedagios(self):
        return self.__pedagios

    def gastos_combustivel(self):
        combustivel = self.km_total / self._opcoes.km_por_litro
        if combustivel < 50:
            return 50
        else:
            return combustivel

    def valores_pedagio(self, *args):
        self.__pedagios = args
    
    def numero_carros(self):
        if self.__quantidade_musicos > 4:
            carros = self.__quantidade_musicos // 4 + 1
        else:
            carros = 1
        return carros

    def total(self):
        combustivel = self.__carros * self.gastos_combustivel()
        cache = self.__quantidade_musicos * self.__valor_cache
        resultado = combustivel + self._opcoes.valor_alimentacao + cache + sum(self.pedagios)
        return resultado