from abc import ABC,abstractmethod
class general_user(ABC):    
    def __init__(self,name,joining_year):
        self.name=name
        self.joining_year=joining_year
    def calculate_years(self):
        return 2025-self.joining_year
    @abstractmethod
    def get_role(self):
        pass
    def show_details(self):
        print(f"Name:{self.name}",f"Role:{self.get_role()}",f"Calculate Years:{self.calculate_years()}")
class Customer( general_user):
    def get_role(self):
        return "Customer"
class Vendor(general_user):
    def get_role(self):
        return "Vendor" 
customer1=Customer("Manu",2020)
vendor1=Vendor("Appu",2022) 
customer1.show_details()
vendor1.show_details()   