marks = []

i=0
while (i<3):
    x = int(input("Enter Marks : "))
    marks.append(x)
    i+=1

result = True
i=0
while (i<3):
    if (marks[i]<33):
        result = False
    i+=1

if (sum(marks)<120):
    result = False

if (result):
    print("Pass")
else:
    print("Fail")
