def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro ao dividir por zero"
    return a / b

print("Calculadora")
print("1 - Somar")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha: ")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if opcao == "1":
    print(soma(n1, n2))
elif opcao == "2":
    print(subtracao(n1, n2))
elif opcao == "3":
    print(multiplicacao(n1, n2))
elif opcao == "4":
    print(divisao(n1, n2))