n = int(input("Enter The Value of N (odd): "))
while (n%2==0):
    n = int(input("Please Enter Odd Number : "))


for i in range(n):
    print('*',end='')
print('')

for i in range(int(n/2)):
    for j in range(int(n/2) - i):
        print('*',end='')
    for j in range(2*i+1):
        print(' ',end='')
    for j in range(int(n/2) - i):
        print('*',end='')
    print('')

for i in range(1,int(n/2)):
    for j in range(i+1):
        print('*',end='')
    for j in range(n-2-2*i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')

for i in range(n):
    print('*',end='')


# *******
# *** ***
# **   **
# *     *
# **   **
# *** ***
# *******