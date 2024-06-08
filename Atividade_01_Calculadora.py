def nome_programa():
    print("Calculadora")

def exibir_opcoes():
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair\n")

def finalizar_programa():
    print("Encerrando o programa...")

def opcao_invalida():
    print("Opção invalida!\n")

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

def escolher_operacao():
    try:
        operacao_escolhida = int(input("Escolha uma operação: "))

        if operacao_escolhida in [1, 2, 3, 4]:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
        
        if operacao_escolhida == 1:
            resultado = somar(x, y)
            print(f"Resultado: {resultado}\n")
        elif operacao_escolhida == 2:
            resultado = subtrair(x, y)
            print(f"Resultado: {resultado}\n")
        elif operacao_escolhida == 3:
            resultado = multiplicar(x, y)
            print(f"Resultado: {resultado}\n")
        elif operacao_escolhida == 4:
            resultado = dividir(x, y)
            print(f"Resultado: {resultado}\n")
        elif operacao_escolhida == 5:
            finalizar_programa()
            return False
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    return True

def main():
    continuar = True
    while continuar:
        nome_programa()
        exibir_opcoes()
        continuar = escolher_operacao()

main()
