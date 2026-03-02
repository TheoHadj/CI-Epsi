# def main():
#     print("Hello, World!")

    
# if(__name__ == "__main__"):
#     main()


class Character:
    def __init__(self, name):
        self.name = name
        # self.hp = hp
        self.hp = 10
        # self.attack_power = attack_power
        self.attack_power=1
        
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, target):
        target.take_damage(self.attack_power)
        return self.attack_power