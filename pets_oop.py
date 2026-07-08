#🟢 Project 1: Pet (Perfect for today)
#Create a class called Pet.
#Each pet should have:
#name
#animal
#age
#Create 2 pet objects.
#Add methods:
#introduce()
#birthday() (increases age by 1)
#speak() (prints anything suitable for that animal)
#Call all the methods on both pets.

class Pet:
         
          def __init__(self, name, animal, age):
                     self.name = name
                     self.animal = animal
                     self.age = age

pet1 = Pet("Luz", "Dog", 4)
pet2 = Pet("Bella", "Cat", 8)

def introduce(self):
       print(f"Hi, I am  {self.name}")  
               
pet1.introduce()      
pet2.introduce()
         
def birthday(self):
       print(self.age + 1)
           
pet1.birthday()
pet2.birthday()
    
def speak(self):   
       print("I am your pet hehe")     
         
pet1.speak()   
pet2.speak()