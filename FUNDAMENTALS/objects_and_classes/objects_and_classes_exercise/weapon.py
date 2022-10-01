class Weapon:
    bullets = 0

    def __init__(self, number_of_bullets:int):
        self.number_of_bullets = number_of_bullets
        self.bullets += number_of_bullets

    def shoot(self):
        message = ""
        if self.bullets > 0:
            self.bullets -= 1
            message = "shooting..."
        else:
            message = "no bullets left"

        return message

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
