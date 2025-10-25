a = 80

def fun():
    global a # It also change the global a 
    a = 3
    print(a)

fun()
print(a)