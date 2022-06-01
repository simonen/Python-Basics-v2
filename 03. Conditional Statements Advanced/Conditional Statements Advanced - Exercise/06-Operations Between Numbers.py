number_a = int(input())
number_b = int(input())
operator = input()

result = 0
even_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = number_a + number_b
    elif operator == "-":
        result = number_a - number_b
    elif operator == "*":
        result = number_a * number_b
    if result % 2 == 0:
        even_odd = "even"
    print(f"{number_a} {operator} {number_b} = {result} - {even_odd}")
if operator == "/" or operator == "%":
    if number_b == 0:
        print(f"Cannot divide {number_a} by zero")
    else:
        if operator == "/":
            result = number_a / number_b
            print(f"{number_a} {operator} {number_b} = {result:.2f}")
        elif operator == "%":
            result = number_a % number_b
            print(f"{number_a} {operator} {number_b} = {result}")

