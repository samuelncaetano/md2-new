# Solicita ao usuário que insira um número natural
var = int(input("Digite um número natural: "))

# Define uma função recursiva para imprimir números de 1 até var
def rec(n):
    if n > var:  # Caso base: se n for maior que var, a função retorna
        return
    print(n)  # Imprime o número atual
    rec(n + 1)  # Chamada recursiva: imprime o próximo número

# Verifica se o número inserido é menor que 1
if var < 1:
    # Se o número for menor que 1, imprime uma mensagem de erro
    print("Deve-se digitar um número natural (maior ou igual a 1).")
else:
    # Se o número for um número natural, chama a função recursiva começando de 1
    rec(1)