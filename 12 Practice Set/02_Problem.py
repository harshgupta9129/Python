l = [1,2,3,4,5,6,7,8,9,10]

pre = [3,5,7]
for index, item in enumerate(l):
    if index+1 in pre:
        print(item)