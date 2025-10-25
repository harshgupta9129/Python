with open("./09 Practice Set./this.txt") as f:
    content = f.read()

with open("./09 Practice Set./this_copy.txt", 'w') as f:
    f.write(content)