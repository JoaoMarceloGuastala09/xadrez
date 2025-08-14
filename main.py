# Códigos de cor ANSI
RESET = "\033[0m"
AMARELO = "\033[33m"
VERDE = "\033[32m"

# Tabuleiro inicial
tabuleiro = [
    ["T","C","B","R","D","B","C","T"],
    ["P","P","P","P","P","P","P","P"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["p","p","p","p","p","p","p","p"],
    ["t","c","b","r","d","b","c","t"]
]

def colorir(peca):
    """Retorna a peça colorida: brancas amarelas, pretas verdes"""
    if peca == " ":
        return " "
    if peca.isupper():  # Peça branca
        return AMARELO + peca + RESET
    else:               # Peça preta
        return VERDE + peca + RESET

def mostrar_tabuleiro(tab):
    print("\n    0   1   2   3   4   5   6   7")  # Cabeçalho colunas
    print("   " + "---"*8)
    for i, linha in enumerate(tab):
        linha_formatada = " | ".join(colorir(p) for p in linha)
        print(f"{i} | {linha_formatada} |")
        print("   " + "---"*8)
    print()

def mover(tab, origem, destino):
    linha_o, col_o = origem
    linha_d, col_d = destino
    peca = tab[linha_o][col_o]

    if peca == " ":
        print("❌ Não há peça nessa posição!")
        return False
    
    tab[linha_d][col_d] = peca
    tab[linha_o][col_o] = " "
    return True

# Loop principal
while True:
    mostrar_tabuleiro(tabuleiro)
    try:
        origem = tuple(map(int, input("Origem (linha coluna): ").split()))
        destino = tuple(map(int, input("Destino (linha coluna): ").split()))
    except ValueError:
        print("❌ Entrada inválida! Digite dois números separados por espaço.")
        continue
    
    mover(tabuleiro, origem, destino)
