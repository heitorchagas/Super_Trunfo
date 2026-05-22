import random


# Estrutura de cada carta: [Nome, Velocidade máx (km/h), Tanque (litros), Ano criação]

GABARITO_ATRIBUTOS = ["Nome", "Velocidade máxima (km/h)", "Tanque de combustível (litros)", "Ano de criação"]

BARALHO_COMPLETO = [
    ["Ferrari F40",        324, 110, 1987],
    ["Lamborghini Diablo", 330, 90,  1990],
    ["Porsche 911 GT1",    310, 90,  1996],
    ["McLaren F1",         386, 80,  1992],
    ["Bugatti Veyron",     407, 100, 2005],
    ["Koenigsegg CCX",     395, 70,  2006],
    ["Pagani Zonda",       345, 98,  1999],
    ["Ford GT",            330, 70,  2004],
    ["Dodge Viper",        306, 70,  1991],
    ["Aston Martin DB9",   299, 80,  2003],
    ["Chevrolet Corvette", 298, 68,  1997],
    ["Nissan GT-R",        315, 74,  2007],
    ["Toyota Supra",       285, 70,  1993],
    ["Honda NSX",          270, 65,  1990],
    ["Mazda RX-7",         250, 60,  1992],
    ["Alfa Romeo 8C",      292, 72,  2007],
    ["BMW M3 GTR",         305, 68,  2001],
    ["Mercedes SLR",       334, 97,  2003],
    ["Lotus Elise",        240, 40,  1996],
    ["Subaru Impreza WRX", 255, 60,  2001],
]


# ==============================================================
# FUNÇÕES AUXILIARES
# ==============================================================

def exibir_carta(carta):
    print(f"\n  Carta: {carta[0]}")
    for i in range(1, len(GABARITO_ATRIBUTOS)):
        print(f"    [{i}] {GABARITO_ATRIBUTOS[i]}: {carta[i]}")


def escolher_atributo(carta, nome_jogador):
    exibir_carta(carta)
    while True:
        try:
            escolha = int(input(f"\n  {nome_jogador}, escolha o atributo (1 a {len(GABARITO_ATRIBUTOS)-1}): "))
            if 1 <= escolha <= len(GABARITO_ATRIBUTOS) - 1:
                return escolha
            else:
                print(f"  Digite um número entre 1 e {len(GABARITO_ATRIBUTOS)-1}.")
        except ValueError:
            print("  Entrada inválida. Digite um número.")


def embaralhar_e_distribuir(baralho):
    copia = [carta[:] for carta in baralho]
    random.shuffle(copia)
    meio = len(copia) // 2
    jogador_1 = copia[:meio]
    jogador_2 = copia[meio:]
    return jogador_1, jogador_2


def exibir_placar(nome1, mao1, nome2, mao2, espera):
    print(f"\n  Placar — {nome1}: {len(mao1)} cartas | {nome2}: {len(mao2)} cartas | Monte de espera: {len(espera)} cartas")



# MODO SINGLE PLAYER (humano vs computador)
def turno_single(mao_humano, mao_pc, espera, nome_humano, rodada):
    print(f"\n{'='*50}")
    print(f"  RODADA {rodada}")
    print(f"{'='*50}")

    carta_humano = mao_humano[0]
    carta_pc = mao_pc[0]

    escolha = escolher_atributo(carta_humano, nome_humano)

    attr_nome = GABARITO_ATRIBUTOS[escolha]
    val_humano = carta_humano[escolha]
    val_pc = carta_pc[escolha]

    print(f"\n  Atributo escolhido: {attr_nome}")
    print(f"  {nome_humano}: {val_humano}  |  Computador: {val_pc}  (carta: {carta_pc[0]})")

    cartas_rodada = [mao_humano.pop(0), mao_pc.pop(0)] + espera[:]
    espera.clear()

    if val_humano > val_pc:
        print(f"\n  {nome_humano} venceu a rodada!")
        mao_humano.extend(cartas_rodada)
    elif val_pc > val_humano:
        print(f"\n  Computador venceu a rodada!")
        mao_pc.extend(cartas_rodada)
    else:
        print("\n  ═ Empate! Cartas vão para o monte de espera.")
        espera.extend(cartas_rodada)


def jogar_single(nome_humano, baralho):
    mao_humano, mao_pc = embaralhar_e_distribuir(baralho)
    espera = []
    rodada = 1

    print(f"\n  Iniciando partida: {nome_humano} vs Computador")
    print(f"  Cada jogador começa com {len(mao_humano)} cartas.\n")

    while len(mao_humano) > 0 and len(mao_pc) > 0:
        exibir_placar(nome_humano, mao_humano, "Computador", mao_pc, espera)
        turno_single(mao_humano, mao_pc, espera, nome_humano, rodada)
        rodada += 1
        input("\n  [Enter para continuar...]")

    if len(mao_humano) > 0:
        print(f"\n  {nome_humano} VENCEU O JOGO!")
        return nome_humano
    else:
        print("\n  COMPUTADOR VENCEU O JOGO!")
        return "Computador"



# MODO DOIS JOGADORES PVP (humano vs humano)
def turno_dual(mao_j1, mao_j2, espera, nome_j1, nome_j2, rodada, vez):
    print(f"\n{'='*50}")
    print(f"  RODADA {rodada} — Vez de: {[nome_j1, nome_j2][vez]}")
    print(f"{'='*50}")

    carta_j1 = mao_j1[0]
    carta_j2 = mao_j2[0]

    if vez == 0:
        nome_ativo = nome_j1
        escolha = escolher_atributo(carta_j1, nome_ativo)
    else:
        nome_ativo = nome_j2
        escolha = escolher_atributo(carta_j2, nome_ativo)

    attr_nome = GABARITO_ATRIBUTOS[escolha]
    val_j1 = carta_j1[escolha]
    val_j2 = carta_j2[escolha]

    print(f"\n  Atributo escolhido: {attr_nome}")
    print(f"  {nome_j1}: {val_j1}  |  {nome_j2}: {val_j2}")

    cartas_rodada = [mao_j1.pop(0), mao_j2.pop(0)] + espera[:]
    espera.clear()

    if val_j1 > val_j2:
        print(f"\n   {nome_j1} venceu a rodada!")
        mao_j1.extend(cartas_rodada)
        return 0
    elif val_j2 > val_j1:
        print(f"\n   {nome_j2} venceu a rodada!")
        mao_j2.extend(cartas_rodada)
        return 1
    else:
        print("\n  ═ Empate! Cartas vão para o monte de espera.")
        espera.extend(cartas_rodada)
        return vez


def jogar_dual(nome_j1, nome_j2, baralho):
    mao_j1, mao_j2 = embaralhar_e_distribuir(baralho)
    espera = []
    rodada = 1
    vez = 0  # 0 = jogador 1 escolhe, 1 = jogador 2 escolhe

    print(f"\n  Iniciando partida: {nome_j1} vs {nome_j2}")
    print(f"  Cada jogador começa com {len(mao_j1)} cartas.\n")

    while len(mao_j1) > 0 and len(mao_j2) > 0:
        exibir_placar(nome_j1, mao_j1, nome_j2, mao_j2, espera)
        vez = turno_dual(mao_j1, mao_j2, espera, nome_j1, nome_j2, rodada, vez)
        rodada += 1
        input("\n  [Enter para continuar...]")

    if len(mao_j1) > 0:
        print(f"\n {nome_j1} VENCEU O JOGO!")
        return nome_j1
    else:
        print(f"\n {nome_j2} VENCEU O JOGO!")
        return nome_j2



# RANKING
ARQUIVO_RANKING = "ranking.txt"

def carregar_ranking():
    ranking = []
    try:
        with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(";")
                    if len(partes) == 2:
                        ranking.append([partes[0], int(partes[1])])
    except FileNotFoundError:
        pass
    return ranking


def salvar_ranking(ranking):
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        for entrada in ranking:
            f.write(f"{entrada[0]};{entrada[1]}\n")


def registrar_vitoria(nome_vencedor):
    ranking = carregar_ranking()
    encontrado = False
    for entrada in ranking:
        if entrada[0] == nome_vencedor:
            entrada[1] += 1
            encontrado = True
            break
    if not encontrado:
        ranking.append([nome_vencedor, 1])
    # Ordenar por vitórias (decrescente) — sem sorted(), usando bubble sort
    n = len(ranking)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ranking[j][1] < ranking[j+1][1]:
                ranking[j], ranking[j+1] = ranking[j+1], ranking[j]
    salvar_ranking(ranking)


def exibir_ranking():
    ranking = carregar_ranking()
    print("\n  ══════════════════════════════")
    print("  ║        RANKING DE VITÓRIAS   ║")
    print("  ══════════════════════════════")
    if not ranking:
        print("  ║  Nenhuma partida registrada. ║")
    else:
        for i, entrada in enumerate(ranking):
            linha = f"  ║  {i+1}. {entrada[0]} — {entrada[1]} vitória(s)"
            print(linha)
    print("  ══════════════════════════════")


# ==============================================================
# MENU PRINCIPAL
# ==============================================================

def menu_principal():
    print("\n" + "="*50)
    print("       BEM-VINDO AO SUPER TRUNFO DE CARROS")
    print("="*50)
    print("  [1] Single Player (vs Computador)")
    print("  [2] Dual Player   (vs Outro Jogador)")
    print("  [3] Ver Ranking")
    print("  [4] Sair")
    print("="*50)
    return input("  Escolha uma opção: ").strip()


def main():
    while True:
        opcao = menu_principal()

        if opcao == "1":
            nome = input("\n  Digite seu nome: ").strip() or "Jogador"
            vencedor = jogar_single(nome, BARALHO_COMPLETO)
            registrar_vitoria(vencedor)

        elif opcao == "2":
            nome1 = input("\n  Nome do Jogador 1: ").strip() or "Jogador 1"
            nome2 = input("  Nome do Jogador 2: ").strip() or "Jogador 2"
            vencedor = jogar_dual(nome1, nome2, BARALHO_COMPLETO)
            registrar_vitoria(vencedor)

        elif opcao == "3":
            exibir_ranking()

        elif opcao == "4":
            print("\n  Até a próxima!\n")
            break

        else:
            print("\n  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


