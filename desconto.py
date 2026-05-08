class SemDesconto:
    def aplicar(self, valor):
        return valor


class DescontoPercentual:
    def __init__(self, percentual):
        self.percentual = percentual

    def aplicar(self, valor):
        desconto = valor * (self.percentual / 100)
        return valor - desconto


class DescontoCupom:
    def __init__(self, valor_cupom):
        self.valor_cupom = valor_cupom

    def aplicar(self, valor):
        valor_final = valor - self.valor_cupom

        if valor_final < 0:
            return 0

        return valor_final


class CalculadoraDesconto:
    def __init__(self, estrategia_desconto):
        self.estrategia_desconto = estrategia_desconto

    def calcular(self, valor):
        return self.estrategia_desconto.aplicar(valor)
