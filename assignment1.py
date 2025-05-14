class Bender:
    def intro(self):
        print("Hello, I am a bender.")
        
class Fire(Bender):
    def __init__(self, name):
        self.name = name
        super().intro()
        print(f"My name is {self.name}, I am a fire bender. Kaboom! Kaboom! 🔥🔥")

class Air(Bender):
    def __init__(self, name):
        self.name = name
        super().intro()
        print(f"My name is {self.name}, I am an air bender. Whoosh! Whoosh! 🌪️🌪️")

class Water(Bender):
    def __init__(self, name):
        self.name = name
        super().intro()
        print(f"My name is {self.name}, I am a water bender. Splash! Splash! 🌊🌊")

class Earth(Bender):
    def __init__(self, name):
        self.name = name
        super().intro()
        print(f"My name is {self.name}, I am an earth bender. Boom! Boom! ⛰️⛰️")

person1 = Fire("Zuko")
person2 = Water("Katara")
person3 = Air("Tenzin")
person4 = Earth("Toph")