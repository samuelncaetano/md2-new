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

# Calcula e imprime o MDC dos dois números
print(f"O MDC de {a} e {b} é {mdc(a, b)}")