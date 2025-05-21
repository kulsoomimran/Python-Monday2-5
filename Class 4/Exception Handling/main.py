# --- BASIC TRY-EXCEPT ---

try:
    num = int(input("Enter a number: "))
    print("Number entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# --- MULTIPLE EXCEPTIONS ---

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An error occurred:", e)

# --- FINALLY BLOCK ---

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
