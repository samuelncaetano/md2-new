# Solicita ao usuário que insira um número inteiro não negativo
var = int(input("Digite um número inteiro não negativo: "))

# Define uma função recursiva para calcular o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:  # Caso base: o fatorial de 0 ou 1 é 1
        return 1
    return n * fatorial(n - 1)  # Chamada recursiva: n * fatorial de (n-1)

# Verifica se o número inserido é negativo
if var < 0:
    # Se o número for negativo, imprime uma mensagem de erro
    print("Fatorial não é definido para números negativos.\n")
else:
    # Se o número for não negativo, calcula e imprime o fatorial
    print(f"O fatorial de {var} é {fatorial(var)}")