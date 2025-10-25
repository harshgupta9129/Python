with open("./09 Practice Set./dockey.txt", 'r+') as f:
    data = f.read().replace("Donkey","#####")
    f.seek(0)
    f.write(data)
    f.truncate()