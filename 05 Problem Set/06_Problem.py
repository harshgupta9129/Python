dic = {}

i = 0
while (i<4):
    name = input("Enter Your Name : ")
    lang = input("Enter Your Favorite Language : ")
    dic.update({name : lang})
    i+=1

print(dic)