class Employee:
    
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_name =emp_name
        self.emp_id = emp_id
        self.emp_salary =emp_salary
        self.emp_department = emp_department
        
        
    def get_name(self):
        return self.emp_name
    
    def get_id(self):
        return self.emp_id
    
    
    def get_salary(self):
        return self.emp_salary
    
       
    def get_department(self):
        return self.emp_department
    
    
    def set_name(self):
         self.emp_name=newName
    
    def set_id(self):
         self.emp_id=newId
    
    
    def set_salary(self):
         self.emp_salary= newSalary
    
       
    def set_department(self):
         self.emp_department=newDepartment
    
    
                
    def descrip(self):
            return f"employee name {self.emp_name} is {self.emp_id} the salary is {self.emp_salary}"
        

    
    

    
    
