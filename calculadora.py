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

def operacoes_basicas():
    print(50*"-")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Voltar")
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
        print("Voltando...")
    else:
        print("Escolha inválida!")

def subconjunto_proprio():
    conjuntoA = []
    conjuntoB = []
    cont = 0
    qnt_numA = input("Digite quantos números o conjunto A deve ter: ")
    while cont < int(qnt_numA):
        numA = input("Digite um número para o conjunto A: ")
        conjuntoA.append(numA)
        cont += 1
    print(f"Conjunto A: {conjuntoA}")
    cont = 0
    qnt_numB = input("Digite quantos números o conjunto B deve ter: ")
    while cont < int(qnt_numB):
        numB = input("Digite um número para o conjunto B: ")
        conjuntoB.append(numB)
        cont += 1
    print(f"Conjunto B: {conjuntoB}")
    if (conjuntoA <= conjuntoB) == True:
        print("O conjunto A é subconjunto próprio de B")
    else:
        print("O conjunto A não é subconjunto próprio de B")

def uniao():
    print("falta tudo")

def interseccao():
    print("falta tudo")

def diferenca():
    print("falta tudo")

def conjuntos_numericos():
    print(50*"-")
    print("Selecione uma das opções:")
    print("1. Verificar se A é subconjunto próprio de B")
    print("2. Realizar operação de união")
    print("3. Calcular intersecção")
    print("4. Calcular diferença")
    print("5. Voltar")
    escolha = input("Digite sua escolha: ")
    if escolha == '1':
        subconjunto_proprio()
    elif escolha == '2':
        uniao()
    elif escolha == '3':
        interseccao()
    elif escolha == '4':
        diferenca()
    elif escolha == '5':
        print("Voltando")
    else:
        print("Escolha inválida!")

def funcoes_segundo_grau():
    print("falta tudo")

def funcoes_exponenciais():
    print("falta tudo")

def matrizes():
    print("falta tudo")

def sair():
    print("Saindo...")
    exit()

def menu_opcoes():
    print(50*"-")
    print("Escolha uma das opções:")
    print("1. Operações básicas")
    print("2. Conjuntos numéricos")
    print("3. Funções do segundo grau")
    print("4. Funções exponenciais")
    print("5. Matrizes")
    print("6. Sair")
    opcao = input("Digite sua escolha: ")
    if opcao == '1':
        operacoes_basicas()
    elif opcao == '2':
        conjuntos_numericos()
    elif opcao == '3':
        funcoes_segundo_grau()
    elif opcao == '4':
        funcoes_exponenciais()
    elif opcao == '5':
        matrizes()
    elif opcao == '6':
        sair()
    else:
        print("Escolha inválida! Escolha uma das opções.")

while True:
    menu_opcoes()