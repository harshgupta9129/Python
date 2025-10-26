class student:
    def name(self):
        name = input("Enter The Name of Student : ")
        self.name = name

    def marks(self):
        marks = input("Enter The Marks of Student {}: ".format(self.name))
        self.marks = marks

    def ph_no(self):
        ph_no = input("Enter The Phone Number of Student {}: ".format(self.name))
        self.ph_no = ph_no

    def info(self):
        return "The Name of Student is {} and he got marks {} and his phone number is {}".format(self.name, self.marks, self.ph_no)
    

id1 = student()
id1.name()
id1.marks()
id1.ph_no()
print(id1.info())