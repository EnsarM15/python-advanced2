class Animal:
    def sound(self):
        print("sound of animal")


class Dog(Animal):

    def sound(self):
        print("woof woof")


class Cat(Animal):

    def sound(self):
        print("meow meow")


animal1 = Animal()
animal1.sound()

animal2 = Dog()
animal2.sound()

animal3 = Cat()
animal3.sound()