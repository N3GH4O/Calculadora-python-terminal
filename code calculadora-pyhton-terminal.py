# calculadora_simples.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por nada"
    return a / b

def mostrar_menu():
    print("Calculadora em Python")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Digite sua opção: ")

    if opcao == '0':
        print("Calculadora fechando. Até a próxima!")
        break

    if opcao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = somar(num1, num2)
            elif opcao == '2':
                resultado = subtrair(num1, num2)
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
            elif opcao == '4':
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}\n")

        except ValueError:
            print("Por favor, digite apenas números!\n")
    else:
        print("Opção inválida. Tente novamente.\n")
