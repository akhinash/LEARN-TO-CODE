# class Grandparent:
#     def house(self):
#         print("Grandparent's house")
# class Parent(Grandparent):
#     def car(self):
#         print("Parent's car")
# class Child(Parent):
#     def bike(self):
#         print("Child's bike")
        
# c = Child()
# c.bike()  
# c.car()
# c.house()

# class A:
#     def show(self):
#         print("class A")
# class B(A):
#     def show(self):
#         super().show()
#         print("class B")
# class C(A):
#     def show(self):
#         super().show()
#         print("class C")
# class D(B,C):
#     def show(self):
#         super().show()
#         print("class D")
# obj = D()
# obj.show()  


# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
# d=Dog()
# d.sound()
# d.bark()
# print(".........")
# c=Cat()
# c.sound()
# c.meow()


# class animal:
#     def show(self):
#         print("Animal Kingdom")
# class mammal(animal):
#     def feature(self):
#         print("Warm Blooded")
# class bird(animal):
#     def feature(self):
#         print("can fly")
# class bat(mammal,bird):
#     def special_feature(self):
#         print("can fly and warm blooded")
        
# b=bat()
# b.show()
# b.feature()
# b.special_feature()

class duck:
    def sound(self):
        print("Quack Quack")
class dog:
    def sound(self):
        print("Bark Bark")
class cat:
    def sound(self):
        print("Meow Meow")
        
def make_sound(animal):
    animal.sound()
    
duck=duck()
dog=dog()
cat=cat()   

make_sound(duck)
make_sound(dog)         
make_sound(cat)