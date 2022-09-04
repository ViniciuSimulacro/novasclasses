from time import sleep

class Carro:
    def __init__(self, motor,velocidade,aceleracao,combustivel):
        self.motor = motor
        self.velocidade = velocidade
        self.aceleracao = aceleracao
        self.combustivel = combustivel

    def carro_andando(self):
        while self.combustivel > 10:
            self.combustivel -= 5
            if self.combustivel == 10:
                print('Estamos ficando sem gasolina')
                abastecer = str(input('Você quer abastecer? (s/n): '))
                if abastecer == 's':
                    quantidade = int(input('Quanto você quer abastecer? (multiplo de 10): '))
                    self.combustivel = quantidade
                    
                else:
                    print('Carro parando por falta de gasolina em 3....')
                    break
            print('Carro andando ainda....')

            print(f'Ainda resta {self.combustivel} litros de combustível')
            sleep(0.7)
        sleep(0.8)    
        print('2.....')
        sleep(0.8)
        print('1....')
        sleep(0.8)
        print('O carro parou....rsrs')



        
meucarango = Carro('v8',180,5,30)
meucarango.carro_andando()