import random

class Sniper:
    def __init__(self,name):
        self.name = name
        self.health = 100

    def shoot (self,sniper):
        sniper.health -=20


sniper1 = Sniper('Alex')
sniper2 = Sniper('Jeck')

choses = (sniper1,sniper2)


while True:

    shooter=random.choice(choses)

    if shooter ==sniper1:
        shot = sniper2
    else:
        shot= sniper1

    shooter.shoot(shot)
    print(f'Shooter {shooter.name} is shooting {shot.name} has {shot.health} health points')


    if sniper1.health == 0:
        print(f'{sniper1.name} is dead. {sniper2.name} is won')
        break
    elif sniper2.health == 0:
        print(f'{sniper2.name} is dead. {sniper1.name} is won')
        break

    else:
        continue