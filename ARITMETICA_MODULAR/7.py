# Solicita ao usuário o tamanho da tabela
n = int(input("Digite o tamanho da tabela: "))

# Função para criar a tabela Z_n para adição modular
def criar_tabela_zn(n):
    tabela = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = (i + j) % n
            linha.append(valor)
        tabela.append(linha)
    return tabela

# Função para imprimir a tabela de forma legível
def imprimir_tabela(tabela):
    for linha in tabela:
        print(' '.join(map(str, linha)))

# Cria a tabela Z_n
tabela = criar_tabela_zn(n)

# Imprime a tabela Z_n
imprimir_tabela(tabela)