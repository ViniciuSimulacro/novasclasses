class Carro:
    def __init__(self,cor, motor, gasolina):
        self.__cor = cor
        self.__motor = motor #opções: 'funcionando' ou 'quebrado'
        self.__gasolina = gasolina

    @property
    def cor_do_carro(self):
        a = self.__cor
        return print(f' o carro é da cor {a}')

    @cor_do_carro.setter
    def mudando_a_cor(self, novacor = str):
        self.__cor = novacor

    def muda_cor(self):
        print(f'A cor do seu carro é {self.__cor}')
        mudando_cor = input(str('Para qual cor vc gostaria de mundar: '))
        self.__cor = mudando_cor
        print(f'Agora a cor de seu carro é {self.__cor}')

    def conserto_de_motor(self):
        print(f'O seu motor esta {self.__motor}')
        if self.__motor == 'quebrado':
            consertar = str(input('Gostaria de consertar seu motor (s/n): '))
            if consertar == 's':
                self.__motor = 'funcionando'
                print(f'Você gastou R$ 3.000,00 para consertar o seu motor, agora ele esta {self.__motor}')
            if consertar == 'n':
                print('Então quero ver você mesmo consertar....rs')

    def consulta_gasolina(self):
        print(f'O seu carro tem {self.__gasolina} litros!')
        if self.__gasolina <= 10:
            print('Você precisa abastercer!')
        else:
            print('Você ainda tem gasolina pra andar!')

    def muda_gasolina(self):
        print(f'O seu carro tem {self.__gasolina} litros!')
        colocar_gasolina = int(input('Voce gostaria de estar com quantos litros no tanque: '))
        self.__gasolina = colocar_gasolina
        if self.__gasolina < 10:
            print('O carro vai parar...')
        if self.__gasolina > 10:
            print('O carro ainda deve andar bastante!)')