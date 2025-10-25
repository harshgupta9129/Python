try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 

# Else code only run when try code successfully executed
else:
    print("I am inside else")