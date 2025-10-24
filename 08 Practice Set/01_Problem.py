def maximum(a,b,c):
    maxi = a
    if (a<=b):
        if (b<=c):
            maxi = c
        else:
            maxi = b
    else:
        if (a<=c):
            maxi = c
        else:
            maxi = a
    return maxi

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

print(maximum(a,b,c))