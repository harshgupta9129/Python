n = int(input("Enter The Value of N : "))

ans = 1
for i in range(2,n+1):
    ans*=i

print(f"The Factorial of {n} is {ans}")