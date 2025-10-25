class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The Class Attribute of a is {cls.a}")

e1 = employee()
e1.a = 45
e1.show()
