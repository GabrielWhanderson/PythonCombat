"""ATUALIZAÇÕES: - corrigido bug de manter 3 turnos ao jogar de novo na dif insana
                 - adicionado arma 5
                 - correção dos avisos "outer scope" e definiçõa de parametros
                 - alteração no display das armas"""
#Definições base-----------
import random
jogadores = {}
dado_virt = True
buff_suporte = 0


#funções--------------------
def escolher_dificuldade(num_jog: int) -> tuple[int, str, int]:
    while True:
        try:
            dif = int(input("ESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
            if dif == 1:
                return num_jog * 8, 'FÁCIL', 2
            elif dif == 2:
                return num_jog * 10, 'NORMAL', 2
            elif dif == 3:
                return num_jog * 12, 'DIFÍCIL', 2
            elif dif == 4:
                return num_jog * 18, 'INSANO', 3
            else:
                print("Dificuldade inexistente! Tente novamente.")
        except ValueError:
            print("Dificuldade inválida! Por favor, digite um número.")


def armas_lista() -> int:

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
                descricaolista()
                break
            else:
                print("\nArma inexistente! Por favor, escolha um número entre 1 e 5.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, Insira um número.")
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


def rolagem_dados() -> tuple[int, int, int]:
    acerto = 1

    def rolar_dado() -> int:
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
        return dado

    def calculo_armas(dado: int, acerto: int) -> tuple[int, int]:
        dano = 0
        match v:
            case 1:
                dano = dado + 2
            case 2:
                dano = 1 if dado <= 3 else 7
            case 3:
                dano = dado * 2 if a % 2 == 1 else dado
            case 4:
                dano = dado - 2
            case 5:
                dano = dado
                acerto = 6
            case _:
                print('erro bizarro')
        return dano + buff_suporte, acerto

    def chance_critico(dano: int, acerto: int) -> tuple[int, int]:
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

#Cálculo da dificuldade----------
    while True:
        vida_boss, nome_dif, turnos = escolher_dificuldade(num_jog)
        buff_suporte = 0

#Escolha de armas-----------------
        for x in range(0, num_jog, 1):
            armas_lista()
        print(f"Dificuldade: [{nome_dif}] - Vida do boss: {vida_boss}HP")

#Sistema de turnos----------------
        for a in range(0, turnos, 1):
            print(f"\n\n\nTURNO {a + 1}")
            for k, v in jogadores.items():
                critico, dano, acerto = rolagem_dados()

#Cálculo das armas----------
                vida_boss -= dano
                if critico <= acerto:
                    print(f"\nDANO CRÍTICO! {dano} de dano! VIDA RESTANTE: {vida_boss}HP\n")
                else:
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
