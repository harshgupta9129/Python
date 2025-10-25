class Programmer:
    company = "Microsoft"
    def __init__ (self, name, role, age):
        self.name = name
        self.role = role
        self.age = age
    
harsh = Programmer("Harsh Gupta", "Web Developer", 20)
print(harsh.name, harsh.role, harsh.age, harsh.company)
