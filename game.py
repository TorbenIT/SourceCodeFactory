class Enemy: #just a template for many objects
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + " life left")

zombie = Enemy()
boss = Enemy()
zombie.attack()
boss.attack()
zombie.check_life()
boss.check_life()