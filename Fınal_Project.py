
class Employees():
    def __init__(self,name,age):
        self.name=name 
        self.age=age    
        self.lang=set()

    def add_language(self):
        language=input("Please enter language that you can speak")
        self.lang.add(language)
        return self.lang
    
    def who_am_I(self):
        print(f"My name is {self.name}.I'm {self.age} years old.I'm a employee at this company.")
        print(f"I can speak {self.lang}")

class Manager():
    def __init__(self,name,age):
        self.name=name 
        self.age=age    
        self.lang=set()

    def add_language(self):
        language=input("Please enter language that you can speak")
        self.lang.add(language)
        return self.lang
    
    def who_am_I(self):
        print(f"My name is {self.name}.I'm {self.age} years old.I'm manager at this company.")
        print(f"I can speak {self.lang}")



ahmet=Employees("Ahmet",25)
ahmet.add_language()
ahmet.add_language()
ahmet.who_am_I()

serpil=Manager("Serpil",32)
serpil.add_language()
serpil.add_language()
serpil.who_am_I()