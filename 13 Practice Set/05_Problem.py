from functools import reduce

maximum = lambda a,b : max(a,b)

l = [7,2,6,3,0,1,7]
ans = reduce(maximum, l)
print(ans)