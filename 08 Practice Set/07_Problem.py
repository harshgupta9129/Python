l = ["Harsh", "Rohan", "Rahul"]

def rem(l,word):
    for i in range(len(l)):
        l[i] = l[i].strip(word)
    return l

print(rem(l,'h'))