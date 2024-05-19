#Projeto: Calculadora RMC
#Alunos: Arthur Rodrigues Pansera e Stefany Carlos de Oliveira
#Turma: C

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero!"

def calculadora():
    while True:
        print(50*"-")
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        escolha = input("Digite sua escolha: ")
        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == '1':
                print(f"Resultado: {adicao(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == '4':
                while num2 == 0:
                    print("Opção inválida! Impossível dividir por 0!")
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                print(f"Resultado: {divisao(num1, num2)}")
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Escolha inválida! Escolha uma das opções.")

calculadora()