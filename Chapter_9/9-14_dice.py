from random import randint

class Die:
    def __init__(self, sides=6):
        if sides < 2:
            raise ValueError("A die must have at least two sides.")
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

six_sided = Die()
ten_sided = Die(10)
twenty_sided = Die(20)

print("Six-sided die:", [six_sided.roll_die() for _ in range(10)])
print("Ten-sided die:", [ten_sided.roll_die() for _ in range(10)])
print("Twenty-sided die:", [twenty_sided.roll_die() for _ in range(10)])
