from functools import reduce

l = []
for i in range(1,11):
    l.append(i*7)

def vertical_st (a,b):
    return "{}\n{}".format(a,b)

ans = reduce(vertical_st, l)
print(ans)
