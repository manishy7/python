weight = int(input("weight: "))
unit = input('L(bs) or K(kg)')
if unit.upper() == 'L': #upper will convert whatever the user enters into upper case
    converted = weight + 0.45
    print(f"your weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"your weight is {converted} pounds")