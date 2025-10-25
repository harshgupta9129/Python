class Employee:
    salary = 40000
    increment = 20

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100
    

e1 = Employee()
print(e1.salaryafterincrement)

e1.salaryafterincrement = 40000
print(e1.increment)
