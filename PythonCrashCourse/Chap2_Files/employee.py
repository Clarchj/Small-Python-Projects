class employee():
        def __init__(self,first_name,last_name,annual_salary):
                self.first_name=first_name
                self.last_name=last_name
                self.annual_salary=annual_salary
        def give_raise(self,increase_ammount=5000):
                """give raise to specific employee
                """
                self.increase_ammount=increase_ammount
                self.salary_increase_total = increase_ammount + self.annual_salary
                return f"Current salary: {self.salary_increase_total}$"
                
JaneDoe=employee('Jane','Doe',5000)
print(type(JaneDoe.give_raise(5000)))