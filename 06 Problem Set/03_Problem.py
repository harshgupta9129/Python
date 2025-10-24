message = input("Enter Message : ")

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

if (spam1 in message or spam2 in message or spam3 in message or spam4 in message):
    print("Spam...!")
else:
    print("No Worry...!")