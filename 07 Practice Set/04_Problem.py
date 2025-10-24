a = int(input("Enter A Number : "))

isprime = True
for i in range(2,a):
    if (a%i==0):
        isprime = False

if (isprime):
    print(f"{a} is a prime number")
else:
    print(f"{a} is not prime number")