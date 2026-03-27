def soma(a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    return a / b

print ("=== Calculadora ===")

num1 = float(input("Primeiro Número"))
num2 = float(input("Segundo Número"))

operacao = input ("Escolhe operação (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", soma(num1, num2))
elif operacao == "-":
    print("Resultado:", subtracao(num1, num2))
elif operacao == "*":
    print("Resultado:", multiplicacao(num1, num2))
elif operacao == "/":
    print("Resultado:", divisao(num1, num2))
else:
    print("Operação inválida")