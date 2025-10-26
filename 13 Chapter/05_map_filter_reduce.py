from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]

square = lambda x : x*x

sq_value = list(map(square, l))
print(sq_value)

# Filter Example
def even(n):
    if (n%2):
        return False
    return True

# If Return True Value Then Input Value goes in final
onlyeven = list(filter(even, l)) 
print(onlyeven)

# Reduce Example

sum = lambda a,b : a+b
print(reduce(sum, l))