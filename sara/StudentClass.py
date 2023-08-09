from Person import Person
class Student(Person):
    #Consrractor
    
    def __init__(self, sname, sage,year):
        super(). __init__(sname, sage)
        
        self.acadeic__year =year
    def say_hi(self):
        return f"Helloo{self.name} as Student"
    