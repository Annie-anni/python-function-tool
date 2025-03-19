from random import randint

class Die:
    def __init__(self,sides = 20):
        self.sides = sides

    def roll_die(self):
        result = randint(1,self.sides)
        print(f"Rolling a {self.sides} -sided die:{result}")

twenty_sided_die = Die()
for _ in range(10):
    twenty_sided_die.roll_die()