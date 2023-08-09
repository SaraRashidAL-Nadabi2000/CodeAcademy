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
    
    T1=Teatcher("sara",33,2025)
    print(T1.say_hi())
   
  
    
    print(Person2.descrip())
    
    print(Sara.get_name())
    Sara.set_name("Sara AL-Nadabi")
    print (Sara.get_name())
    print(Sara.descrip())
    Sara.run()
    Sara.laugh()
    Person2.laugh()
      
main()