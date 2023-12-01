

#Class ninja
class Ninja:
    def __init__(self, first_name,last_name,treats,pet_food,pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet

    def walk(self): # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.play()

        return self
    def feed(self): # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self
    def bathe(self): # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self