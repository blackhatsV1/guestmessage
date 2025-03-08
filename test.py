class Merlin():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print("===============================================")
        print(f"I am {self.name}. I have {self.power} power.")
        print("===============================================")

    def addPower(self):
        self.power += 100
        print("=========================================")
        print(f"Power Up! My power is now {self.power}.")
        print("=========================================")


hero = Merlin("Merlin", 100)

while True:
    print()
    print("Choose Action:")
    print("1. Introduce Hero")
    print("2. Power up hero")
    choice = input(">> ")
    match choice:
        case "1":
            hero.introduce()
            continue
        case "2":
            hero.addPower()
            continue
        case "3":
            print("exit")
            break
        case "":
            print("Empty")
            continue
        case _:
            print("invalid. Try Again.")
            continue