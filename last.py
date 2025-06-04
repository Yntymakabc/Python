class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Aibek(Animal):
    def __init__(self):
        pass

a = Animal("aibek", 34)
print(a.name)
b =