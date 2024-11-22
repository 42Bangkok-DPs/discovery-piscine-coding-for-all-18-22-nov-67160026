first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
result = first_number * second_number
print(f"{first_number} x {second_number} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is both positive and negative.")
[22:54]
03
cell03
number = int(input("Enter a number less than 25: "))
if number > 25:
    print("Error")
else:

    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1
[22:54]
00
[22:54]
number = int(input("Enter a number: "))
for i in range(10):
    result = i * number
    print(f"{i} x {number} = {result}")
[22:54]
01
[22:55]
def main():
    userinput = input("What you gotta say? : ")
    while True:

        if userinput == "STOP": 
            break 
        else:
            userinput = input("I got that! Anything else? : ")

if name == "main":
    main()
[22:55]
02 