class Person:
    #constractor to crea Objects
    #initiliz instance variable
        def __init__(self,name,age=20):
         self.name = name
         self.age = age
         
        def say_hi(self):
            return f"Helloo{self.name} as Person"
    #use term of encapsulation
        def get_name(self):
            return self.name
        def get_age(self):
            return self.age
    #setter /mutiotur method
        def set_name(self,newName):
            self.name=newName
        def set_age(self,newAge):
            self.age=newAge
            
            
        def run(self):
            print(self.name, "is running")
                
        def descrip(self):
            return f"Person name {self.name} is {self.age} years old"
        
        def laugh(self):
            print(self.name,"say hahahahahaha")
