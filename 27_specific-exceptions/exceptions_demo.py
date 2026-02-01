s = input("Enter a number: ")

try:
    x = int(s)
    print("OK:", x)
except ValueError:
    print("Please enter digits only (e.g., 123).")
