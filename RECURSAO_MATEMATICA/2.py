# Solicita ao usuário que insira o número de termos da sequência de Fibonacci
num = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Define uma função recursiva para calcular o n-ésimo número de Fibonacci
def Fibonacci(n):
    if n == 1 or n == 2:  # Caso base: Fibonacci(1) e Fibonacci(2) = 1
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)  # Chamada recursiva: soma dos dois termos anteriores

# Exibe os números da sequência de Fibonacci até o n-ésimo termo
print(f"Sequência de Fibonacci até o {num}º termo:")
for i in range(1, num + 1):  # Itera de 1 até num (inclusive)
    print(Fibonacci(i), end=" ")  # Imprime o i-ésimo número de Fibonacci, seguido de um espaço
print("")  # Imprime uma nova linha ao final