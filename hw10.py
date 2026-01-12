from  abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year
    def account_age(self):
        return 2025-self.account_year 
    @abstractmethod
    def get_role(self):
        pass  
class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Guest Usser:{self.name},Account Age:{self.account_age()}years"
admin1=Admin("Nikhil",2018)
guest1=Guest("Aparna",2019)
print("Role:",admin1.get_role())
print("Account Age:",admin1.account_age())
print()
print("Role:",guest1.get_role())
print("Account Age:",guest1.account_age())
print(guest1)
    
         
        