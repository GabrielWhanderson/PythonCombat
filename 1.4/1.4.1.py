"""ATUALIZAÇÕES: - Adicionado "nome_dif" e mudança no texto inicial do hp do boss
                 - Adicionado arma 4
                 - corrigido opção de digitar n° maior de 6 no dado
                 - nova mensagem para caso de 0 de dano"""
#Definições base-----------
import random
jogadores = {}
turnos = 2
nome_dif = ''
dado_virt = True
escolhaArma = -1
dano = 0
vida_boss = 0
num_jog = 0
buff_suporte = 0


#funções--------------------
def escolher_dificuldade() -> tuple[int, str, int]:
    global vida_boss, nome_dif, turnos
    while True:
        try:
            dif = int(input("ESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
            match dif:
                case 1:
                    vida_boss = num_jog * 8
                    nome_dif = 'FÁCIL'
                    break
                case 2:
                    vida_boss = num_jog * 10
                    nome_dif = 'MÉDIO'
                    break
                case 3:
                    vida_boss = num_jog * 12
                    nome_dif = 'DIFÍCIL'
                    break
                case 4:
                    vida_boss = num_jog * 18
                    turnos = 3
                    nome_dif = 'INSANO'
                    break
                case _:
                    print("\nDificuldade inexistente! Tente novamente.")
                    continue
        except ValueError:
            print("\nDificuldade inválida! Por favor, digite um número.")
            continue
    return vida_boss, nome_dif, turnos


def armas_lista() -> int:
    global escolhaArma
    global buff_suporte
    while True:
        try:
            ler_descricoes = int(input(f'JOGADOR {x + 1}, ESCOLHA UMA ARMA:'
                                      f'\n0 - ABRIR DESCRIÇÕES'
                                      f'\n1 - ESPADA'
                                      f'\n2 - MACHADO'
                                      f'\n3 - ARCO E FLECHA'
                                      f'\n4 - LIVRO ENCANTADO'
                                       '\n'))
            if ler_descricoes in [1, 2, 3, 4]:
                escolhaArma = ler_descricoes
                if escolhaArma == 4:
                    buff_suporte += 1
                    print(buff_suporte)
                break
            elif ler_descricoes == 0:
                descricaolista()
                break
            else:
                print("\nArma inexistente! Por favor, escolha um número entre 1 e 4.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, Insira um número.")
            continue
    jogadores[f"JOGADOR {x + 1}"] = escolhaArma
    return escolhaArma


def descricaolista() -> int:
    global escolhaArma
    while True:
        try:
            escolhaArma = int(input(f'\n\nJOGADOR {x + 1}, ESCOLHA UMA ARMA:'
                                f'\n1 - ESPADA: Adiciona +2 de dano ao rolamento.'
                                f'\n2 - MACHADO: Caso a rolagem seja alta, dá 7 de dano. Caso contrário, dá 1 de dano.'
                                f'\n3 - ARCO E FLECHA: A cada 2 turnos, dá o dobro de dano.'
                                f'\n4 - LIVRO ENCANTADO: diminui -1 ao seu próprio dano, mas aumenta +1 aos seus aliados.'
                                 '\n'))
            if escolhaArma not in [1, 2, 3, 4]:
                print("\nArma inexistente! Por favor, escolha um número entre 1 e 4.")
                continue
            else:
                break
        except ValueError:
            print("\nEntrada inválida! Insira um número.")
        continue
    return escolhaArma


def rolagem_dados(buff_suporte: int):
    if dado_virt:
        input(f"{k.upper()}, ROLE O DADO (Pressione ENTER): ")
        dado = (random.randint(1, 6))
        print(f'VOCÊ TIROU {dado}!')
    else:
        while True:
            try:
                dado = int(input(f"{k.upper()}, DIGITE A ROLAGEM DO DADO: "))
                if dado > 6 or dado < 1:
                    print("\nPor favor, digite um número entre 1 e 6")
                    continue
                break
            except ValueError:
                print('\nValor inválido!')

    def calculo_armas() -> int:
        global dano
        match v:
            case 1:
                dano = (dado + 2) + buff_suporte
            case 2:
                if dado <= 3:
                    dano = 1 + buff_suporte
                else:
                    dano = 7 + buff_suporte
            case 3:
                if a % 2 == 1:
                    dano = (dado * 2) + buff_suporte
                else:
                    dano = dado + buff_suporte
            case 4:
                dano = dado - 1
                if buff_suporte >= 2:
                    dano += buff_suporte - 1
            case _:
                print('erro bizarro')
        return dano
    calculo_armas()


#Início----------------
print('-------------RPG Game-------------')
try:
    while True:
        opcJogo = input('\nVOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: ').strip().lower()
        if opcJogo in ['s', 'sim']:
            dado_virt = False
            break
        elif opcJogo in ['n', 'nao', 'não']:
            break
        else:
            print('\nerro! por favor, digite novamente!\n')
            continue

    while True:
        try:
            num_jog = int(input('INSIRA O NÚMERO DE JOGADORES: '))
            if num_jog < 1:
                print('O jogo precisa ter ao menos 1 jogador!\n')
                continue
            break
        except ValueError:
            print('Por favor, digite um número inteiro.\n')
            continue

#Cálculo da dificuldade----------
    while True:
        escolher_dificuldade()
        buff_suporte = 0

#Escolha de armas-----------------
        for x in range(0, num_jog, 1):
            armas_lista()
        print(f"Dificuldade: [{nome_dif}] - Vida do boss: {vida_boss}HP")

#Sistema de turnos----------------
        for a in range(0, turnos, 1):
            print(f"\n\n\nTURNO {a + 1}")
            for k, v in jogadores.items():
                rolagem_dados(buff_suporte)
#Cálculo das armas----------
                vida_boss -= dano
                print(f"\n{dano} de dano! VIDA RESTANTE: {vida_boss}HP\n" if dano != 0
                    else f"\nVOCÊ NÃO DEU DANO! VIDA RESTANTE: {vida_boss}HP\n")
                if vida_boss <= 0:
                    break

        #Condições de fim-----------
        print("\n\nVITÓRIA! O monstro foi derrotado! :)\n" if vida_boss <= 0
              else "\n\nDERROTA! O monstro é forte demais... ;()\n")
        continuar = input('\nDESEJA JOGAR NOVAMENTE? SE SIM, PRESSIONE [s]: \n\n').strip().lower()
        if continuar in ['s', 'sim']:
            continue
        else:
            print('ATÉ MAIS!')
            break

except KeyboardInterrupt:
    exit('jogo interrompido.')
