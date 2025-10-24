def convert(cel):
    return cel*1.8 + 32

cel = int(input("Enter The Temperature in Celsius : "))
print(f"After Coversion in Fahrenheit is {convert(cel)}")