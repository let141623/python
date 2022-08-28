class calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

    def somar(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 + self.num2
        return self.resultado

    def subtrair(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 - self.num2
        return self.resultado

    def multiplicar(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 * self.num2
        return self.resultado

    def dividir(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 / self.num2
        return self.resultado

    def expoente(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 ** self.num2
        return self.resultado

    def resto(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = self.num1 % self.num2
        return self.resultado

def continuar(entrada):
    if entrada:
        return True
    else:
        return False

def menu():
    opc = {1:'Adição',
           2: 'Subtração',
           3: 'Multiplicação',
           4: 'Divisão',
           5: 'Exponenciação',
           6: 'Módulo (resto)'}

    calc = calculadora ()        #varivevel para chamar a class
    print("""Você quer realizar qual operação matemática?
    1 -> Adição
    2 -> Subtração
    3 -> Multiplicação
    4 -> Divisão
    5 -> Exponenciação
    6 -> Módulo (resto)
    Digite o número desejado e aperte ENTER""")
    calcular = True
    while calcular:
        opcao = input('\n Escolha a opção desejada (,1,2,3,4,5 ou 6)')
        if not(opcao in '1 2 3 4 5 6'):
            print('Opção escolhida é invalida!')
            continue
        else:
            opcao = int(opcao)
            print(f"A operacão escolhida é {opc[opcao]}")
            print ('Apenas números inteiros são válidos,ok?')
        if opcao ==1:
            num1 = int(input('Digite o penultipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.somar(num1,num2)
            print(f'O valor da SOMA da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
        elif opcao == 2:
            num1 = int(input('Digite o penúltipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.subtrair(num1, num2)
            print(f'O valor da SUBTRAÇÃO da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
        elif opcao == 3:
            num1 = int(input('Digite o penúltipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.multiplicar(num1, num2)
            print(f'O valor da MULTIPLICAÇÃO da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
        elif opcao == 4:
            num1 = int(input('Digite o penúltipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.dividir(num1, num2)
            print(f'O valor da DIVISÃO da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
        elif opcao == 5:
            num1 = int(input('Digite o penúltipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.expoente(num1, num2)
            print(f'O valor da EXPOENCIAÇÃO da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
        elif opcao == 6:
            num1 = int(input('Digite o penúltipo número do seu RU'))
            num2 = int(input('Digite o último numero do seu RU:'))
            resultado = calc.resto(num1, num2)
            print(f'O valor do RESTO da operação é: {resultado}.')
            calcular = continuar(input('Digite algo para continuar ou aperte ENTER para sair da Calculadora da Letícia!'))
            print('Calculo encerrado, muito obrgada!')
menu()








