def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum:", add(x, y))

    print("Difference:", subtract(x, y))
    print("Quotient:", divide(x,y))
    print("Product: ", multiply(x,y))
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
    
def multiply(a, b):
    return a * b
    

