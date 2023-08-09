from Person import Person
class Teatcher(Person):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.exp_years = year
    
    def say_hi(self):
        return f"Hi {self.name} as Teatcher"
    
