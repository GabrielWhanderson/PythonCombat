"""ATUALIZAÇÕES: - novo modo de jogo: battle royale (mínimo 2 jogadores)
                 - elif chain no escolher_dificuldade reformulada em match case
                 - corrigido bug ao esolher cajado várias vezes em sequência (buff acumulado)
                 - alteração no display de alguns textos (\n)
                 - ValueError expection na lista de minigames"""
#Definições base-----------
import random
jogadores = {}
escolhaArma = 0


#funções--------------------
def escolher_dificuldade(num_jog: int) -> tuple[int, str, int]: #define o nível de dificuldade do boss

    while True:
        try:
            dif = int(input("\nESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
            match dif:
                case 1:
                    return num_jog * 8, 'FÁCIL', 2
                case 2:
                    return num_jog * 10, 'NORMAL', 2
                case 3:
                    return num_jog * 12, 'DIFÍCIL', 2
                case 4:
                    return num_jog * 18, 'INSANO', 3
                case _:
                    print("Dificuldade inexistente! Tente novamente.")
        except ValueError:
            print("Dificuldade inválida! Por favor, digite um número.")


def armas_lista(x: int) -> int: #Cada jogador escolhe sua arma (sem descrição)
    global buff_suporte, escolhaArma
    while True:
        try:
            ler_descricoes = int(input(f'\nJOGADOR {x + 1}, ESCOLHA UMA ARMA:'
                                      f'\n0 - ABRIR DESCRIÇÕES          3 - ARCO E FLECHA'
                                      f'\n1 - ESPADA                    4 - LIVRO ENCANTADO'
                                      f'\n2 - MACHADO                   5 - CAJADO'
                                       '\n'))
            if ler_descricoes in [1, 2, 3, 4, 5]:
                escolhaArma = ler_descricoes
                if escolhaArma == 4:
                    buff_suporte += 1
                break
            elif ler_descricoes == 0:
                descricaolista(x)
                break
            else:
                print("\nArma inexistente! Por favor, escolha um número entre 1 e 5.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, Insira um número.")
    jogadores[f"JOGADOR {x + 1}"] = escolhaArma
    return escolhaArma


def descricaolista(x: int) -> int: #abre a lista de descrições das armas
    global escolhaArma
    while True:
        try:
            escolhaArma = int(input(f'\n\nJOGADOR {x + 1}, ESCOLHA UMA ARMA:'
                                f'\n1 - ESPADA: Adiciona +2 de dano ao lançamento.'
                                f'\n2 - MACHADO: Caso o lançamento seja alta, dá 7 de dano. Caso contrário, dá 1 de dano.'
                                f'\n3 - ARCO E FLECHA: A cada 2 turnos, dá o dobro de dano.'
                                f'\n4 - LIVRO ENCANTADO: se enfraquece em -1 de dano, mas aumenta +1 aos seus aliados.'
                                f'\n5 - CAJADO: Tem maior chance de acertos críticos.'
                                '\n'))
            if escolhaArma not in [1, 2, 3, 4, 5]:
                print("\nArma inexistente! Por favor, escolha um número entre 1 e 5.")
                continue
            else:
                break
        except ValueError:
            print("\nEntrada inválida! Insira um número.")
    return escolhaArma


def rolagem_dados(k, v: int, a: int) -> tuple[int, int, int]: #Sistema completo do cálculo de dano
    acerto = 1

    def rolar_dado() -> int: #Decide o valor do lançamento
        if dado_virt: #Dado virtual randomizado
            input(f"{k.upper()}, ROLE O DADO (Pressione ENTER): ")
            dado = (random.randint(1, 6))
            print(f'Você tirou {dado}!')
        else: #Dado físico
            while True:
                try:
                    dado = int(input(f"{k.upper()}, DIGITE A ROLAGEM DO DADO: "))
                    if dado > 6 or dado < 1:
                        print("\nPor favor, digite um número entre 1 e 6")
                        continue
                    break
                except ValueError:
                    print('\nValor inválido!')
        return dado

    def calculo_armas(dado: int, acerto: int) -> tuple[int, int]: #Calcula as fórmulas de dano de cada arma
        dano = 0
        match v:
            case 1: #Adiciona +2 de dano ao lançamento (ESPADA)
                dano = dado + 2
            case 2: #Caso o lançamento seja alta, dá 7 de dano. Caso contrário, dá 1 de dano (MACHADO)
                dano = 1 if dado <= 3 else 7
            case 3: #A cada 2 turnos, dá o dobro de dano (ARCO E FLECHA)
                dano = dado * 2 if a % 2 == 1 else dado
            case 4: #diminui -1 ao seu próprio dano, mas aumenta +1 aos seus aliados (LIVRO ENCANTADO)
                dano = dado - 2
            case 5: #Tem maior chance de acertos críticos (CAJADO)
                dano = dado
                acerto = 6
            case _:
                print('erro bizarro')
        return dano + buff_suporte, acerto

    def chance_critico(dano: int, acerto: int) -> tuple[int, int]: #Calcula a chance de acerto crítico
        critico = random.randint(1, 14)
        if critico <= acerto:
            dano += 1
            while dano % 6 != 0:
                dano += 1
        return critico, dano

    dado = rolar_dado()
    dano, acerto = calculo_armas(dado, acerto)
    critico, dano = chance_critico(dano, acerto)

    return critico, dano, acerto


def inicio() -> tuple[bool, int]: #Definições padrão aplicáveis a todos os minigames
    def escolha_dados() -> bool: #Escolha entre dado virtual ou físico
        global dado_virt
        while True:
            opc_jogo = input('\nVOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: ').strip().lower()
            if opc_jogo in ['s', 'sim']:
                dado_virt = False
                break
            elif opc_jogo in ['n', 'nao', 'não']:
                dado_virt = True
                break
            else:
                print('\nerro! por favor, digite novamente!\n')
                continue
        return dado_virt

    def numero_jogadores() -> int: #Determina o número de jogadores da sessão
        global num_jog
        while True:
            try:
                num_jog = int(input('INSIRA O NÚMERO DE JOGADORES: '))
                if num_jog < 1:
                    print('O jogo precisa ter ao menos 1 jogador!\n')
                    continue
                break
            except ValueError:
                print('Por favor, digite um número inteiro.\n')
        return num_jog
    dado_virt = escolha_dados()
    num_jog = numero_jogadores()
    return dado_virt, num_jog


def boss_battle() -> None: #Primeiro minigame
#Cálculo da dificuldade----------
    while True:
        vida_boss, nome_dif, turnos = escolher_dificuldade(num_jog)
#Escolha de armas-----------------
        for x in range(0, num_jog, 1):
            armas_lista(x)
        print(f"\nDificuldade: [{nome_dif}] - Vida do boss: {vida_boss}HP")
#Sistema de turnos----------------
        for a in range(0, turnos, 1):
            print(f"\n\n\nTURNO {a + 1}", escolhaArma)
            for k, v in jogadores.items():
                critico, dano, acerto = rolagem_dados(k, v, a)

#Cálculo das armas----------
                vida_boss -= dano
                if critico <= acerto:
                    print(f"\nDANO CRÍTICO! {dano} DE DANO! VIDA RESTANTE: {vida_boss}HP\n")
                else:
                    print(f"\n{dano} DE DANO! VIDA RESTANTE: {vida_boss}HP\n" if dano != 0
                          else f"\nVOCÊ NÃO DEU DANO! VIDA RESTANTE: {vida_boss}HP\n")
                if vida_boss <= 0:
                    break

#Condições de fim-----------
        print("\n\nVITÓRIA! O monstro foi derrotado! :)\n" if vida_boss <= 0
              else "\n\nDERROTA! O monstro é forte demais... ;()\n")
        break


def battle_royale() -> None: #Segundo minigame
    jogadores.clear()
#Escolha de armas-----------------
    for x in range(0, num_jog, 1):
        armas_lista(x)
#Sistema de turnos----------------
    turnos = 1
    while len(jogadores) > 1:
        print(f"\n\n\nTURNO {turnos} - Jogadores restantes: {len(jogadores)}")
        turnos += 1
        menor = 999
        eliminado = []
        empate = False
#Eliminação por turno-------------
        for k, v in jogadores.items():
            critico, dano, acerto = rolagem_dados(k, v, turnos)
            if dano < menor:
                menor = dano
                eliminado = k
                empate = False
            elif dano == menor:
                empate = True
            if critico <= acerto:
                print(f"DANO CRÍTICO! {dano} DE DANO!\n")
            else:
                print(f"{dano} DE DANO!\n")
        if empate:
            print("EMPATE! NENHUMA ELIMINAÇÃO.")
        else:
            print(f"JOGADOR ELIMINADO: {eliminado}")
            del jogadores[eliminado]
    print(f"\n\n{k}, VOCÊ É O VENCEDOR!!!\n")


#Início----------------
print('-------------RPG Game-------------')

try:
    dado_virt, num_jog = inicio()
    while True:
        buff_suporte = 0
        gamemode = int(input("\nMODOS DE JOGO:\n1 - Batalha de Chefão\n2 - Battle Royale\n"))
        match gamemode:
            case 1:
                boss_battle()
            case 2:
                if num_jog < 2:
                    print("Mínimo 2 jogadores para este modo!")
                    continue
                else:
                    battle_royale()
            case _:
                print("\nEscolha um modo de jogo existente!")
                continue

        continuar = input('\nVOLTAR AO MENU INICIAL? [s]: \n').strip().lower()
        if continuar in ['s', 'sim']:
            continue
        else:
            break

except KeyboardInterrupt:
    exit('\njogo interrompido.')
except ValueError:
    print("Dificuldade inválida! Por favor, digite um número.")
