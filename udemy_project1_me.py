import random


print("This is a dice simulator")
def game():
    dice = random.randrange(1, 7, 1)
    dicel = {
        1 : "[-------------]\n[             ]\n[      0      ]\n[             ]\n[-------------]",
        2 : "[-------------]\n[             ]\n[    0   0    ]\n[             ]\n[-------------]",
        3 : "[-------------]\n[      0      ]\n[      0      ]\n[      0      ]\n[-------------]",
        4 : "[-------------]\n[    0   0    ]\n[             ]\n[    0   0    ]\n[-------------]",
        5 : "[-------------]\n[    0   0    ]\n[      0      ]\n[    0   0    ]\n[-------------]",
        6 : "[-------------]\n[    0   0    ]\n[    0   0    ]\n[    0   0    ]\n[-------------]"
    }
    print(dicel[dice])
    input("Press Enter and accept the dice")
    game()
game()
