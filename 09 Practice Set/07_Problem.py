with open("./09 Practice Set./log.html", "r") as f:
    count = 0

    line = f.readline()
    while line!='':
        if ("python" in line):
            count+=1
        line = f.readline()
    print(f"The No of Lines in which python is present : {count}")
