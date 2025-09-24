import random
dano = 0
critico = (random.randint(1, 5))
if 1 <= critico <= 2:
    dano += 1
    while dano % 6 != 0:
        dano += 1
print(critico, dano)
