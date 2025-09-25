"""ATUALIZAÇÕES: - Adição das descrições das armas
                 - Correção na exibição da rolagem virtual
                 - Pequenas correções e adições de texto"""
#Definições base-----------
import random
jogadores = {}
turnos = 2
dado_virt = True
escolhaArma = -1
dano = -1
vida_boss = 0

print('-------------RPG Game-------------')
if (input('VOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: ').lower() == 's' or
        'VOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: '.lower() == 'sim'):
    dado_virt = False

num_jog = int(input('INSIRA O NÚMERO DE JOGADORES: '))

#Cálculo da dificuldade----------
dif = int(input("\nESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
match dif:
    case 1:
        vida_boss = num_jog * 8
    case 2:
        vida_boss = num_jog * 10
    case 3:
        vida_boss = num_jog * 12
    case 4:
        vida_boss = num_jog * 18
        turnos = 3
    case _:
        print("Dificuldade inválida")

#Escolha de armas-----------------
for x in range(0, num_jog, 1):
    escolhaArma = int(input(f'JOGADOR {x+1} ESCOLHA UMA ARMA:'
                                            f'\n0 - ABRIR DESCRIÇÕES'
                                            f'\n1 - ESPADA'
                                            f'\n2 - MACHADO'
                                            f'\n3 - ARCO E FLECHA\n'))
    if escolhaArma == 0:
        escolhaArma = int(input(f'\n\n\n1 - ESPADA: Adiciona +2 de dano ao rolamento.'
        f'\n2 - MACHADO: Caso a rolagem seja alta, dá 7 de dano. Caso contrário, dá 1 de dano.'
        f'\n3 - ARCO E FLECHA: A cada 2 turnos, dá o dobro de dano.\n'))
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
            dado = int(input(f"{k.upper()}, DIGITE A ROLAGEM DO DADO: "))

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
                print('erro')
        vida_boss -= dano
        print(f"\n{dano} de dano! VIDA RESTANTE: {vida_boss}HP\n")

#Condições de fim-----------
if vida_boss <= 0:
    print("\n\nVitória!")
else:
    print("\n\nDerrota ;(")
