# IF - ELSE STATEMENTS
print("\nIF - ELSE STATEMENTS")
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is not positive")

# IF - ELIF - ELSE STATEMENTS
print("\nIF - ELIF - ELSE STATEMENTS")
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# NESTED IF STATEMENTS
print("\nNESTED IF STATEMENTS")
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 != 0:
        print("Positive Odd Number")
    else:
        print("Positive Even Number")
else:
    print("Negative Number")

# FOR LOOP
print("\nFOR LOOP")
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

# WHILE LOOP
print("\nWHILE LOOP")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# NESTED LOOPS
print("\nNESTED LOOPS")
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)