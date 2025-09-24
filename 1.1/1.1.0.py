#Definições base-----------
import random
jogadores = {}
turnos = 2
dado_virt = True
dano = -1

if input('VOCÊ TEM UM DADO FÍSICO PARA JOGAR? [s] OU [n]: ').lower() == 's':
    dado_virt = False

num_jog = int(input('INSIRA O NÚMERO DE JOGADORES: '))

#Cálculo da dificuldade----------
dif = int(input("\nESCOLHA UMA DIFICULDADE:\n1 - FÁCIL\n2 - NORMAL\n3 - DÍFICIL\n4 - INSANO (3 turnos)\n"))
match dif:
    case 1:
        vida_boss = num_jog * 7
    case 2:
        vida_boss = num_jog * 8
    case 3:
        vida_boss = num_jog * 10
    case 4:
        vida_boss = num_jog * 18
        turnos = 3
    case _:
        print("Dificuldade inválida")

for x in range(0, num_jog, 1):
    jogadores[f"jogador {x+1}"] = int(input(f'JOGADOR {x+1} ESCOLHA UMA ARMA: '))

print(f"Vida do boss: {vida_boss}HP")

#Sistema de turnos------------
for a in range(0, turnos, 1):
    print(f"\n\n\nTURNO {a+1}")
    for b in range(0, jogadores, 1):
        if dado_virt:
            input(f"JOGADOR {b+1}, ROLE O DADO (Pressione qualquer tecla): ")
            dado = (random.randint(1, 6))
        else:
            dado = int(input(f"JOGADOR {b+1}, DIGITE A ROLAGEM DO DADO: "))

#Cálculo das armas-------
        vida_boss -= dado
        print(f"\n{dado} de dano! VIDA RESTANTE: {vida_boss}HP")

#Condições de fim---------
if vida_boss <= 0:
    print("\nVitória!")
else:
    print("\nDerrota ;(")
