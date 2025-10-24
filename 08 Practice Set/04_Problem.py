def sum(n):
    if (n<=1):
        return n
    return n + sum(n-1)

n = int(input("Enter The Value of N : "))
print(sum(n))