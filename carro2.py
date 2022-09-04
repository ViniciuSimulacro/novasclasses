class Carro:
    def __init__(self,cor, motor, gasolina):
        self.cor = cor
        self.motor = motor #opções: 'funcionando' ou 'quebrado'
        self.gasolina = gasolina

    def muda_cor(self):
        print(f'A cor do seu carro é {self.cor}')
        mudando_cor = input(str('Para qual cor vc gostaria de mundar: '))
        self.cor = mudando_cor
        print(f'Agora a cor de seu carro é {self.cor}')

    def conserto_de_motor(self):
        print(f'O seu motor esta {self.motor}')
        if self.motor == 'quebrado':
            consertar = str(input('Gostaria de consertar seu motor (s/n): '))
            if consertar == 's':
                self.motor = 'funcionando'
                print(f'Você gastou R$ 3.000,00 para consertar o seu motor, agora ele esta {self.motor}')
            if consertar == 'n':
                print('Então quero ver você mesmo consertar essa bosta...rs')

    def abastecer(self):
        print(f'O seu carro tem {self.gasolina} litros!')
        if self.gasolina <= 10:
            print('Você precisa abastercer!')
        else:
            print('Você ainda tem gasolina pra andar!')


meucarango = Carro('azul','quebrado',10)
#meucarango.muda_cor()
#meucarango.conserto_de_motor()
meucarango.abastecer()   