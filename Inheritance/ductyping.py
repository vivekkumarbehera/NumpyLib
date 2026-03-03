#Ductyping
class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")
def make_it_quack(duck):
    duck.quack()
duck = Duck()
person = Person()
make_it_quack(duck)    # Output: Quack!

make_it_quack(person)  # Output: I'm quacking like a duck!