with open("./09 Practice Set./poems.txt") as f:
    st = f.read()
    if ("twinkle" in st):
        print("Yes Twinkle Present in Poem")
    else:
        print("No Twinkle is not present in Poem")
    
