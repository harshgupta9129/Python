def get_value(promt):
    try:
        a = int(input(promt))
        return a
    except:
        print("Please Enter A Integer...!")
        return None
    
n = get_value("Enter A Natural Number : ")
if n is not None:
    with open("./12 Practice Set./Tables.txt", 'a') as f:
        f.write(f"Table of {n}\n")
        for i in range(1,11):
            f.write(f"{n} X {i} = {n*i}\n")
        f.write("\n")
