from dataclasses import replace

number1=float(input("Enter your number:").replace(',','.'))# to make , not crush the system
number2=float(input("Enter your number:").replace(',','.'))#floating is  number with decimals


if number2 < number1:
    print( f"{number1} is bigger then number {number2}")
elif number2 == number1:
    print("gleich")
else:
    print(f"{number1} is smaller then number {number2}")
