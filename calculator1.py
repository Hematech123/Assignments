import math

print("Scientific Calculator")
print("1. Square Root")
print("2. Power")
print("3. Sine")
print("4. Cosine")
print("5. Tangent")
print("6. Logarithm")
print("7. Factorial")

choice = int(input("Enter your choice (1-7): "))

if choice == 1:
    num = float(input("Enter a number: "))
    print("Square Root =", math.sqrt(num))

elif choice == 2:
    base = float(input("Enter base: "))
    exp = float(input("Enter exponent: "))
    print("Result =", math.pow(base, exp))

elif choice == 3:
    angle = float(input("Enter angle in degrees: "))
    print("Sine =", math.sin(math.radians(angle)))

elif choice == 4:
    angle = float(input("Enter angle in degrees: "))
    print("Cosine =", math.cos(math.radians(angle)))

elif choice == 5:
    angle = float(input("Enter angle in degrees: "))
    print("Tangent =", math.tan(math.radians(angle)))

elif choice == 6:
    num = float(input("Enter a number: "))
    print("Log =", math.log10(num))

elif choice == 7:
    num = int(input("Enter a number: "))
    print("Factorial =", math.factorial(num))

else:
    print("Invalid Choice")