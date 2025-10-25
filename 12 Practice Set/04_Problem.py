try:
    a = int(input("Enter Value of a : "))

except:
    print("Please Enter A Integer...!")

else:
    try:
        b = int(input("Enter Value of b : "))
    except:
        print("Please Enter A Integer....!")
    else:
        try:
            print(f"{a} / {b} = {a/b}")
        except ZeroDivisionError as z:
            print(z)
        else:
            print("Successfull Executed Code Without Any Error")