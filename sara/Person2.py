from Person import Person
from StudentClass import Student
from Teatcher import Teatcher
def main():
    Sara = Person("Sara AL-Nadabi",22)
    Person2= Person("Ali")
    print(Sara.say_hi())
    std1=Student("Latifa",18,2001)
    std2=Student("Harith",21,2022)
    print(std1.say_hi())
    print(Student.say_hi(std2))
    
   
   
   E1=Employee("16J1978,Sara,2000,infornation system")
    print(E1.say_hi())
  
    
    print(Person2.descrip())
    
    print(Sara.get_name())
    Sara.set_name("Sara AL-Nadabi")
    print (Sara.get_name())
    print(Sara.descrip())
    Sara.run()
    Sara.laugh()
    Person2.laugh()
      
main()