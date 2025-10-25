try:
    with open("./12 Practice Set./1.txt", 'r') as f1:
        print(f1.read())

    with open("./12 Practice Set./2.txt", 'r') as f2:
        print(f2.read())

    with open("./12 Practice Set./3.txt", 'r') as f3:
        print(f3.read())
    
except Exception as e:
    print("File Not Exist")