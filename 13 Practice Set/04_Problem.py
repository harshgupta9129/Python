l = [3,7,2,5,10,13,15,6,25,20]

multi_5 = lambda x : x%5==0
filter_data = filter(multi_5, l)
print(list(filter_data))