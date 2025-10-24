def printriangle(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print('')

n = int(input("Enter The Value of N : "))
printriangle(n)