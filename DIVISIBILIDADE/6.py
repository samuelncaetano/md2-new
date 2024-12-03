# Solicita ao usuário que insira dois números inteiros
a = int(input("Digite o número A: "))
b = int(input("Digite o número B: "))

# Define a função para calcular o MDC usando o Algoritmo de Euclides
def mdc(a, b):
    while b != 0:
        r = a % b  # Calcula o resto da divisão de a por b
        a = b
        b = r
    return a

# Define a função para calcular o MMC usando o MDC
def mmc(a, b):
    return a * b // mdc(a, b)  # Calcula o MMC usando a fórmula: MMC(a, b) = (a * b) // MDC(a, b)

# Calcula e imprime o MMC dos dois números
print(f"O MMC de {a} e {b} é {mmc(a, b)}")