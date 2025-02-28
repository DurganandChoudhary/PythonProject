import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
def modulus(a, b): return a % b if b != 0 else "Error: Division by zero"
def power(a, b): return a ** b
def square_root(a): return math.sqrt(a) if a >= 0 else "Error: Negative number"
def factorial(a): return math.factorial(a) if a >= 0 else "Error: Negative number"
def logarithm(a): return math.log(a) if a > 0 else "Error: Logarithm of non-positive number"
def sine(a): return math.sin(math.radians(a))
def cosine(a): return math.cos(math.radians(a))
def tangent(a): return math.tan(math.radians(a))

def main():
    while True:
        print("\n🔹 Advanced Calculator Menu:")
        print("1️⃣ Addition")
        print("2️⃣ Subtraction")
        print("3️⃣ Multiplication")
        print("4️⃣ Division")
        print("5️⃣ Modulus (Remainder)")
        print("6️⃣ Exponentiation (Power)")
        print("7️⃣ Square Root")
        print("8️⃣ Factorial")
        print("9️⃣ Logarithm (Natural Log)")
        print("🔟 Trigonometric Functions (sin, cos, tan)")
        print("0️⃣ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("👋 Exiting... Have a great day!")
            break

        elif choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            operations = {
                "1": add(a, b),
                "2": subtract(a, b),
                "3": multiply(a, b),
                "4": divide(a, b),
                "5": modulus(a, b),
                "6": power(a, b),
            }
            print(f"✅ Result: {operations[choice]}")

        elif choice == "7":
            a = float(input("Enter number: "))
            print(f"✅ Result: {square_root(a)}")

        elif choice == "8":
            a = int(input("Enter a non-negative integer: "))
            print(f"✅ Result: {factorial(a)}")

        elif choice == "9":
            a = float(input("Enter a positive number: "))
            print(f"✅ Result: {logarithm(a)}")

        elif choice == "10":
            a = float(input("Enter angle in degrees: "))
            print(f"sin({a}) = {sine(a)}")
            print(f"cos({a}) = {cosine(a)}")
            print(f"tan({a}) = {tangent(a)}")

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
