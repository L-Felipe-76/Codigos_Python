VERIFICADOR = int(0)
decisao_usuario = int(0)
while (VERIFICADOR != 1):
    print("O que você deseja calcular? |1-Soma|2-Subtração|3-Multiplicação|4-Divisão|5-Encerrar|")
    decisao_usuario = int(input("Insira a decisão: "))
    if (decisao_usuario == 1):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print(f'O resultado é {resultado}')
    elif (decisao_usuario == 2):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 - numero2
        print(f'O resultado é {resultado}')
    elif (decisao_usuario == 3):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 * numero2
        print(f'O resultado é {resultado}')
    elif (decisao_usuario == 4):
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 / numero2
        print(f'O resultado é {resultado}')
    elif (decisao_usuario == 5):
        VERIFICADOR = 1
    else:
        print("Número invalido")