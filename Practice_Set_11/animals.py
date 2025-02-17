# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method bark to class 'Dog'.

class Animals:
    def __init__(self):
        self.animals = Animals
        
class Pets(Animals):
    def __init__(self):
        self.pets = Pets
        
class Dog(Pets):
    
    @staticmethod
    def bark():
        print(f"Dogs do Bark!!!")
        
dog_obj = Dog()
dog_obj.bark()