class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print(f"Name:{self.name}")
        print("f Role:{self.role}")
class Trainer(Employee):
    def __init__(self, name, role,specialization):
        super().__init__(name, role)
        self.specialization=specialization
    def display(self):
        print(f"Name:{self.name}")
        print(f"Role:{self.role}")
        print(f"Specialization:{self.specialization}")    
class YogaInstructor(Employee):
    def __init__(self, name, role,yoga_style):
        super().__init__(name, role) 
        self.yoga_style=yoga_style       
    def display(self):
        print(f"Name:{self.name}")
        print(f"Role:{self.role}")
        print(f"Yoga Style:{self.yoga_style}")
class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self, name, role, specialization,yoga_style):
        Employee.__init__(self,name,role)
        self.specialization=specialization
        self.yoga_style=yoga_style
    def display(self):
        print(f"Nmae:{self.name}")
        print(f"Role:{self.role}")
        print(f"Specialization:{self.specialization}")
        print(f"Yoga Style:{self.yoga_style}")
employee=Employee("Kavya","Staff Member")
trainer=Trainer("Deepu","Gym Trainer","Weight Training")
yogainstructor=YogaInstructor("Anjali","Yoga Instructor","Hatha Yoga" )
multitrainer=MultiTrainer("Lalu","Multi Trainer","Cardio","Vinyasa Yoga")
print("Employee Details:")
employee.display()
print("Trainer Details:")
trainer.display()
print("YogaInstructor:")
yogainstructor.display()
print("MultiTrainer:")
multitrainer.display()       
        
           
        
       
        