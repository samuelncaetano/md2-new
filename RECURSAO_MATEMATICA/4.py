# Solicita ao usuário que insira um número inteiro positivo
var = int(input("Digite um número inteiro positivo: "))

# Define uma função recursiva para calcular a soma dos números de 1 até n
def soma(n):
    if n == 0:  # Caso base: a soma de 0 é 0
        return 0
    return n + soma(n - 1)  # Chamada recursiva: n + soma dos números até (n-1)

# Verifica se o número inserido é menor ou igual a 0
if var <= 0:
    # Se o número for menor ou igual a 0, imprime uma mensagem de erro
    print("Deve-se digitar um número inteiro positivo.")
else:
    # Se o número for positivo, calcula e imprime a soma
    print(f"A soma dos números de 1 até {var} é {soma(var)}")