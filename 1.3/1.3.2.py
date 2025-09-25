"""ATUALIZAÇÕES: - opção de jogar de novo
                 - tratamento do KeyboardInterruptError"""
#Definições base-----------
import random
jogadores = {}
turnos = 2
dado_virt = True
escolhaArma = -1
dano = -1
vida_boss = 0
num_jog = 0

#Início-------------
print('-------------RPG Game-------------')
try:
    while True:
        opcJogo = input('VOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: ').strip().lower()
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
        while True:
            try:
                dif = int(input("ESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
                match dif:
                    case 1:
                        vida_boss = num_jog * 8
                        break
                    case 2:
                        vida_boss = num_jog * 10
                        break
                    case 3:
                        vida_boss = num_jog * 12
                        break
                    case 4:
                        vida_boss = num_jog * 18
                        turnos = 3
                        break
                    case _:
                        print("\nDificuldade inexistente! Tente novamente.")
                        continue
            except ValueError:
                print("\nDificuldade inválida! Por favor, digite um número.")
                continue

#Escolha de armas-----------------
        for x in range(0, num_jog, 1):
            while True:
                try:
                    escolhaArma = int(input(f'JOGADOR {x+1}, ESCOLHA UMA ARMA:'
                                            f'\n0 - ABRIR DESCRIÇÕES'
                                            f'\n1 - ESPADA'
                                            f'\n2 - MACHADO'
                                            f'\n3 - ARCO E FLECHA\n'))
                    if escolhaArma in [1, 2, 3]:
                        break
                    elif escolhaArma == 0:
                        try:
                            escolhaArma = int(input(f'\n\nJOGADOR {x + 1}, ESCOLHA UMA ARMA:'
                                                    f'\n1 - ESPADA: Adiciona +2 de dano ao rolamento.'
                                                    f'\n2 - MACHADO: Caso a rolagem seja alta, dá 7 de dano. Caso contrário, dá 1 de dano.'
                                                    f'\n3 - ARCO E FLECHA: A cada 2 turnos, dá o dobro de dano.\n'))
                            if escolhaArma in [1, 2, 3]:
                                break
                            else:
                                pass
                        except ValueError:
                            print("Entrada inválida! Insira um número.")
                        else:
                            print("\nArma inexistente! Por favor, escolha um número entre 1 e 3.")
                except ValueError:
                    print("Entrada inválida. Por favor, Insira um número.")
            jogadores[f"JOGADOR {x + 1}"] = escolhaArma

        print(f"Vida do boss: {vida_boss}HP")

#Sistema de turnos----------------
        for a in range(0, turnos, 1):
            print(f"\n\n\nTURNO {a+1}")
            for k, v in jogadores.items():
                if dado_virt:
                    input(f"{k.upper()}, ROLE O DADO (Pressione qualquer tecla): ")
                    dado = (random.randint(1, 6))
                    print(f'VOCÊ TIROU {dado}!')
                else:
                    while True:
                        try:
                            dado = int(input(f"{k.upper()}, DIGITE A ROLAGEM DO DADO: "))
                            break
                        except ValueError:
                            print('\nValor inválido!')

#Cálculo das armas----------
                match v:
                    case 1:
                        dano = dado + 2
                    case 2:
                        if dado <= 3:
                            dano = 1
                        else:
                            dano = 7
                    case 3:
                        if a % 2 == 1:
                            dano = dado * 2
                        else:
                            dano = dado
                    case _:
                        print('erro bizarro')
                vida_boss -= dano
                print(f"\n{dano} de dano! VIDA RESTANTE: {vida_boss}HP\n")
                if vida_boss <= 0:
                    break

#Condições de fim-----------
        if vida_boss <= 0:
            print("\n\nVITÓRIA! O monstro foi derrotado! :)")
        else:
            print("\n\nDERROTA! O monstro é forte demais... ;(")

        continuar = input('\nDESEJA JOGAR NOVAMENTE? SE SIM, PRESSIONE [s]: \n\n').strip().lower()
        if continuar in ['s', 'sim']:
            continue
        else:
            print('ATÉ MAIS!')
            break
except KeyboardInterrupt:
    print('jogo interrompido.')