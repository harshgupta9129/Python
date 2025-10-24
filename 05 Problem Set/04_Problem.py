s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

print(len(s)) # 2 Becuase of 20, 20.0 trated as same

