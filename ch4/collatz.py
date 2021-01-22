def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1
    return value

prompt = input("Please enter an integer number to see the Collatz sequence: ")
try:
    entry = int(prompt)
    print(entry)
    while entry > 1:
        result = collatz(entry)
        print(result)
        entry = result
except ValueError:
    print("Invalid number. Please enter integer value")

