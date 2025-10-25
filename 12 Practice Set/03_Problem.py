try:
    n = int(input("Enter A Number : "))

except:
    print("Please Enter A Valid")

else:
    l = [f"{n} X {i} = {n*i}" for i in range(1,11)]
    print(l)