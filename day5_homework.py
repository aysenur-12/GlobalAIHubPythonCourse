
class Animals():
    def __init__(self,name,age,legs,breed,color):
        self.name=name
        self.age=age
        self.legs=legs
        self.breed=breed
        self.color=color
    
    def my_breed(self):
        print(f"My breed is {self.breed}") 
 
class Dogs(Animals):
    def __init__(self,name,age,legs,breed,color,extra='loyal'):
     Animals.__init__(self,name,age,legs,breed,color)

     self.extra=extra
     

    def who_am_I (self):
        print(f"I am a dog.My name is {self.name}.People think that I'm {self.extra}.I'm {self.age} years old.I have {self.legs} legs")
        print(f"My color is {self.color}")
        print(Animals.my_breed(self))


class Cats(Animals):
    def __init__(self,name,age,legs,breed,color,extra='sleeper'):
     Animals.__init__(self,name,age,legs,breed,color)

     self.extra=extra

    def who_am_I (self):
        print(f"I am a cat.My name is {self.name}.People think that I'm {self.extra}.I'm {self.age} years old.I have {self.legs} legs")
        print(f"My color is {self.color}")
        print(Animals.my_breed(self))





#Animals('Lucy',2,3,'terrier','gray').my_breed() 
#Dogs('Lucy',2,3,'terrier','brown').who_am_I()
#Cats("Kömür",4,4,'Angora','grey','crazy :)').who_am_I()


