#Projeto: Calculadora RMC
#Alunos: Arthur Rodrigues Pansera e Stefany Carlos de Oliveira
#Turma: C

import numpy as np
import matplotlib.pyplot as plt

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def operacoes_basicas():
    print(50 * "-")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("\nSelecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Voltar")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 1 or escolha > 5:
        escolha = int(input("Opção inválida! Escolha uma das opções: "))
    if escolha == 1:
        print(f"Resultado: {adicao(num1, num2)}")
    elif escolha == 2:
        print(f"Resultado: {subtracao(num1, num2)}")
    elif escolha == 3:
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif escolha == 4:
        while num2 == 0:
            print("Opção inválida! Impossível dividir por 0!")
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Voltando...")

def subconjunto_proprio(conjuntoA, conjuntoB):
    if (conjuntoA <= conjuntoB) == True:
        return print("O conjunto A é subconjunto próprio de B")
    else:
        return print("O conjunto A não é subconjunto próprio de B")

def uniao(conjuntoA, conjuntoB):
    conjuntoC = conjuntoA + conjuntoB
    return print(f"União dos conjuntos A e B: {conjuntoC}")

def interseccao(conjuntoA, conjuntoB):
    conjuntoC = []
    for valor in conjuntoA:
        if valor in conjuntoB:
            conjuntoC.append(valor)
    return print(f"Intersecção dos conjuntos A e B: {conjuntoC}")

def diferenca(conjuntoA, conjuntoB):
    escolha = int(input("Calcular a diferença entre A e B (1) ou B e A (2)? "))
    conjuntoC = []
    while escolha != 1 and escolha != 2:
        escolha = int(input("Opção inválida! Escolha uma das opções: "))
    if escolha == 1:
        for valor in conjuntoA:
            if valor not in conjuntoB:
                conjuntoC.append(valor)
        return print(f"Diferença entre os conjuntos A e B: {conjuntoC}")
    else:
        for valor in conjuntoB:
            if valor not in conjuntoA:
                conjuntoC.append(valor)
        return print(f"Diferença entre os conjuntos B e A: {conjuntoC}")

def conjuntos_numericos():
    print(50 * "-")
    conjuntoA = []
    conjuntoB = []
    cont = 0
    qnt_numA = int(input("Digite quantos números o conjunto A deve ter: "))
    while qnt_numA < 0:
        qnt_numA = int(input("Número inválido! Digite um número maior ou igual a zero: "))
    while cont < int(qnt_numA):
        numA = float(input("Digite um número para o conjunto A: "))
        conjuntoA.append(numA)
        cont += 1
    print(f"Conjunto A: {conjuntoA}")
    cont = 0
    qnt_numB = int(input("Digite quantos números o conjunto B deve ter: "))
    while qnt_numB < 0:
        qnt_numB = int(input("Número inválido! Digite um número maior ou igual a zero: "))
    while cont < int(qnt_numB):
        numB = float(input("Digite um número para o conjunto B: "))
        conjuntoB.append(numB)
        cont += 1
    print(f"Conjunto B: {conjuntoB}")
    print("\nSelecione uma das opções:")
    print("1. Verificar se A é subconjunto próprio de B")
    print("2. Realizar operação de união")
    print("3. Calcular intersecção")
    print("4. Calcular diferença")
    print("5. Voltar")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 1 or escolha > 5:
        escolha = int(input("Opção inválida. Escolha uma das opções: "))
    if escolha == 1:
        subconjunto_proprio(conjuntoA, conjuntoB)
    elif escolha == 2:
        uniao(conjuntoA, conjuntoB)
    elif escolha == 3:
        interseccao(conjuntoA, conjuntoB)
    elif escolha == 4:
        diferenca(conjuntoA, conjuntoB)
    else:
        print("Voltando...")

def raizes(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        parte_real = -b / (2 * a)
        parte_imaginaria = (-delta)**(1 / 2) / (2 * a)
        x1 = f"{parte_real} + {parte_imaginaria}i"
        x2 = f"{parte_real} - {parte_imaginaria}i"
        return print(f"Há duas raízes complexas: [{x1}, {x2}]")
    elif delta > 0:
        x1 = (-b + delta**(1 / 2)) / (2 * a)
        x2 = (-b - delta**(1 / 2)) / (2 * a)
        return print(f"Há duas raízes reais: [{x1}, {x2}]")
    else:
        x = -b / (2 * a)
        return print(f"Há uma raíz real: [{x}]")

def funcao_segundo_grau_x(a, b, c):
    x = float(input("Digite o valor de x: "))
    funcao = a * x**2 + b * x + c
    return print(f"O valor de f({x}) é: {funcao}")

def vertice(a, b, c):
    delta = b**2 - 4 * a * c
    Xv = -b / (2 * a)
    Yv = -delta / (4 * a)
    if Yv > 0:
        return print(f"O vértice da parábola é: V = ({Xv}, {Yv}), sendo o seu ponto de máximo")
    else:
        return print(f"O vértice da parábola é: V = ({Xv}, {Yv}), sendo o seu ponto de mínimo")

def grafico_funcao_segundo_grau(a, b, c):
    eixoX = np.arange(-50, 50, 0.1)
    eixoY = []
    for x in eixoX:
        y = a * x**2 + b * x + c
        eixoY.append(y)
    plt.plot(eixoX, eixoY, label=f"f(x) = {a}x² + {b}x + {c}", color="red")
    plt.title(f"Função do seundo grau: f(x) = {a}x² + {b}x + {c}")
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.grid(True)
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    return plt.show()

def funcoes_segundo_grau():
    print(50 * "-")
    print("Para f(x) = ax² + bx + c:")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    print(f"f(x) = {a}x² + {b}x + {c}")
    print("\nSelecione uma das opções:")
    print("1. Calcular raízes")
    print("2. Calcular função em x pedido")
    print("3. Calcular vértice")
    print("4. Gerar gráfico")
    print("5. Voltar")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 1 or escolha > 5:
        escolha = int(input("Opção inválida. Escolha uma das opções: "))
    if escolha == 1:
        raizes(a, b, c)
    elif escolha == 2:
        funcao_segundo_grau_x(a, b, c)
    elif escolha == 3:
        vertice(a, b, c)
    elif escolha == 4:
        grafico_funcao_segundo_grau(a, b, c)
    else:
        print("Voltando...")

def crescente_ou_decrescente(a):
    if a > 0:
        return print("A função é crescente")
    elif a < 0:
        return print("A função é decrescente")
    else:
        return print("A função é constante")

def funcao_exponencial_x(a, b):
    x = float(input("Digite o valor de x: "))
    funcao = a * (b**x)
    return print(f"O valor de f({x}) é: {funcao}")

def grafico_funcao_exponencial(a, b):
    eixoX = np.arange(-50, 50, 0.1)
    eixoY = []
    for x in eixoX:
        y = a * (b**x)
        eixoY.append(y)
    plt.plot(eixoX, eixoY, label=f"f(x) = {a} * {b}**x", color="red")
    plt.title(f"Função exponencial: f(x) = {a} * {b}**x")
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.grid(True)
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    return plt.show()

def funcoes_exponenciais():
    print(50 * "-")
    print("Para f(x) = a * b**x:")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    while b == 1:
        b = float(input("O valor de b não pode ser igual a 1. Digite outro valor: "))
    print(f"f(x) = {a} * {b}**x")
    print("\nSelecione uma das opções:")
    print("1. Verificar se é crescente ou decrescente")
    print("2. Calcular função em x pedido")
    print("3. Gerar gráfico")
    print("4. Voltar")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 1 or escolha > 4:
        escolha = int(input("Opção inválida. Escolha uma das opções: "))
    if escolha == 1:
        crescente_ou_decrescente(a)
    elif escolha == 2:
        funcao_exponencial_x(a, b)
    elif escolha == 3:
        grafico_funcao_exponencial(a, b)
    else:
        print("Voltando...")

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        return print("Não é possível calcular o determinante pois a matriz não é quadrada")
    if len(matriz) == 2:
        det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        return print(f"O determinante da matriz é: {det}")
    elif len(matriz) == 3:
        valor1 = matriz[0][0] * matriz[1][1] * matriz[2][2]
        valor2 = matriz[0][1] * matriz[1][2] * matriz[2][0]
        valor3 = matriz[0][2] * matriz[1][0] * matriz[2][1]
        diagonal_principal = valor1 + valor2 + valor3
        valor4 = matriz[0][1] * matriz[1][0] * matriz[2][2]
        valor5 = matriz[0][0] * matriz[1][2] * matriz[2][1]
        valor6 = matriz[0][2] * matriz[1][1] * matriz[2][0]
        diagonal_secundaria = valor4 + valor5 + valor6
        det = diagonal_principal - diagonal_secundaria
        return print(f"O determinante da matriz é: {det}")
    else:
        return print("O determinante de matrizes maiores que 2x2 ou 3x3 não está implementado")

def multiplicacao_matrizes(matriz):
    matriz2 = []
    num_linhas2 = int(input("Informe o número de linhas da segunda matriz: "))
    while num_linhas2 <= 0:
        num_linhas2 = int(input("Número inválido! Digite um número maior que zero: "))
    num_colunas2 = int(input("Informe o número de colunas da segunda matriz: "))
    while num_colunas2 <= 0:
        num_colunas2 = int(input("Número inválido! Digite um número maior que zero: "))
    for i in range(num_linhas2):
        linha = []
        for j in range(num_colunas2):
            elemento = float(input(f"Informe M2[{i}][{j}]: "))
            linha.append(elemento)
        matriz2.append(linha)
    for linha in matriz2:
        print(linha)
    if len(matriz[0]) != num_linhas2:
        return print("Não é possível realizar a multiplicação pois as matrizes são de ordens diferentes")
    resultado = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz2[0])):
            elemento = 0
            for k in range(len(matriz2)):
                elemento += matriz[i][k] * matriz2[k][j]
            linha.append(elemento)
        resultado.append(linha)
    for linha in resultado:
        print(linha)

def matriz_transposta(matriz):
    transposta = []
    for j in range(len(matriz[0])):
        linha_transposta = []
        for i in range(len(matriz)):
            linha_transposta.append(matriz[i][j])
        transposta.append(linha_transposta)
    for linha in transposta:
        print(linha)

def matrizes():
    print(50 * "-")
    matriz = []
    num_linhas = int(input("Informe o número de linhas da matriz: "))
    while num_linhas <= 0:
        num_linhas = int(input("Número inválido! Digite um número maior que zero: "))
    num_colunas = int(input("Informe o número de colunas da matriz: "))
    while num_colunas <= 0:
        num_colunas = int(input("Número inválido! Digite um número maior que zero: "))
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Informe M{i}{j}: "))
            linha.append(elemento)
        matriz.append(linha)
    for linha in matriz:
        print(linha)
    print("\nSelecione uma das opções:")
    print("1. Determinante")
    print("2. Multiplicação")
    print("3. Matriz transposta")
    print("4. Voltar")
    escolha = int(input("Digite sua escolha: "))
    while escolha < 1 or escolha > 4:
        escolha = int(input("Opção inválida. Escolha uma das opções: "))
    if escolha == 1:
        determinante(matriz)
    elif escolha == 2:
        multiplicacao_matrizes(matriz)
    elif escolha == 3:
        matriz_transposta(matriz)
    else:
        print("Voltando...")

def menu_opcoes():
    print(50 * "-")
    print("Escolha uma das opções:")
    print("1. Operações básicas")
    print("2. Conjuntos numéricos")
    print("3. Funções do segundo grau")
    print("4. Funções exponenciais")
    print("5. Matrizes")
    print("6. Sair")
    opcao = int(input("Digite sua escolha: "))
    while opcao < 1 or opcao > 6:
        opcao = int(input("Opção inválida. Escolha uma das opções: "))
    if opcao == 1:
        operacoes_basicas()
    elif opcao == 2:
        conjuntos_numericos()
    elif opcao == 3:
        funcoes_segundo_grau()
    elif opcao == 4:
        funcoes_exponenciais()
    elif opcao == 5:
        matrizes()
    else:
        print("Saindo...")
        exit()

while True:
    menu_opcoes()