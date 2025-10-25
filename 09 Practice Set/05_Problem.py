words = ["Donkey", "Bad", "Ganda"]

for word in words:
    with open("./09 Practice Set./dockey.txt", 'r+') as f:
        data = f.read().replace(word,"#"*len(word))
        f.seek(0)
        f.write(data)
        f.truncate()