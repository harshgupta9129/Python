with open("./09 Practice Set./log.html", 'r') as f:
    if ("python" in f.read()):
        print("Yes Python is Present")
    else:
        print("No Python is not present")