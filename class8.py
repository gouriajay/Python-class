class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def show_details(self):
        print(f"Name:{self.name}") 
        print(f"Age:{self.age}")  
        print(f"Employee ID:{self.employee_id}")
class PartTime(Person):
    def __init__(self, name, age,working_hours):
        super().__init__(name, age)       
        self.working_hours=working_hours
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Working Hours:{self.working_hours}")
class Consultant(Employee,PartTime):
    def __init__(self, name, age, employee_id,working_hours,project_name):
        Person.__init__(self,name,age)
        self.employee_id=employee_id
        self.working_hours=working_hours
        self.project_name=project_name
    def show_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Employee Id{self.employee_id}")
        print(f"Working Hours{self.working_hours}")
        print(f"Project Name:{self.project_name}")
person=Person("Anju",25)
employee=Employee("Kiran",30,"EMP120")
partTime=PartTime("Sanju",28,19.5)
consultant=Consultant("Kalyani",27,"CONS407",16.0,"AI Development")

print("Person Details:")
person.show_details()
print("Employee Details:")
employee.show_details()
print("Part_Time Details:")
partTime.show_details()
print("Consultant Details:")
consultant.show_details()
        
        
        
               
           
          
            
        
    