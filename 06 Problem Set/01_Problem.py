arr = []

i = 0
while (i<4):
    x = int(input("Enter Number : "))
    arr.append(x)
    i+=1

maximum = arr[0]
i=1
while (i<4):
    if (arr[i]>maximum):
        maximum = arr[i]
    i+=1

print(maximum)