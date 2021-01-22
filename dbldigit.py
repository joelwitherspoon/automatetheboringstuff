digit = input("Please enter a single number, 0-9: ")
int(digit)
doubledigit = int(digit) * 2
if int(doubledigit) >= 10:
    print(str(digit))
    print(str(doubledigit))
    sum = 1 + int(doubledigit) % 10
else:
    print(str(digit))
    sum = int(doubledigit)
print("Sum of the digits is " + str(sum))
