import random

class Robot:
    def __init__(self, name, attack, hp, accuracy):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.accuracy = accuracy
        self.stunned = False

    def attack_enemy(self, enemy):
        if self.stunned:
            print(f"{self.name} is stunned and cannot attack!")
            self.stunned = False  # Stun lasts for one turn
            return
        
        if random.random() <= self.accuracy:
            damage = random.randint(self.attack - 5, self.attack + 5)
            enemy.hp -= damage
            print(f"{self.name} attacks {enemy.name} for {damage} damage! {enemy.name} has {enemy.hp} HP left.")
        else:
            print(f"{self.name} missed the attack!")

    def regen_health(self):
        heal = random.randint(5, 15)
        self.hp += heal
        print(f"{self.name} regenerates {heal} HP! Now has {self.hp} HP.")
    
    def use_stun(self, enemy):
        if random.random() < 0.3:  # 30% chance to stun
            enemy.stunned = True
            print(f"{self.name} stuns {enemy.name}! {enemy.name} will miss the next turn.")
        else:
            print(f"{self.name} tried to stun {enemy.name} but failed!")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start(self):
        round_num = 1
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"\n--- Round {round_num} ---")
            
            # Robot 1's turn
            action = random.choice(["attack", "regen", "stun"])
            if action == "attack":
                self.robot1.attack_enemy(self.robot2)
            elif action == "regen":
                self.robot1.regen_health()
            elif action == "stun":
                self.robot1.use_stun(self.robot2)

            if self.robot2.hp <= 0:
                print(f"{self.robot2.name} has been defeated! {self.robot1.name} wins!")
                break
            
            # Robot 2's turn
            action = random.choice(["attack", "regen", "stun"])
            if action == "attack":
                self.robot2.attack_enemy(self.robot1)
            elif action == "regen":
                self.robot2.regen_health()
            elif action == "stun":
                self.robot2.use_stun(self.robot1)

            if self.robot1.hp <= 0:
                print(f"{self.robot1.name} has been defeated! {self.robot2.name} wins!")
                break
            
            round_num += 1

# Example Usage
robot1 = Robot("Robo-X", attack=20, hp=100, accuracy=0.8)
robot2 = Robot("Mecha-Z", attack=18, hp=110, accuracy=0.85)
game = Game(robot1, robot2)
game.start()
