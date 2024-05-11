num_one = int(input())
num_two = int(input())
symbol_operation = input()

result = 0
result_check_up = ""

if num_two == 0:
    print(f"Cannot divide {num_one} by zero")
    exit()
elif symbol_operation == "+":
    result = num_one + num_two
    if result % 2 == 0:
        result_check_up = "even"
    else:
        result_check_up = "odd"
elif symbol_operation == "-":
    result = num_one - num_two
    if result % 2 == 0:
        result_check_up = "even"
    else:
        result_check_up = "odd"
elif symbol_operation == "*":
    result = num_one * num_two
    if result % 2 == 0:
        result_check_up = "even"
    else:
        result_check_up = "odd"
elif symbol_operation == "/":
    result = num_one / num_two
    print(f"{num_one} / {num_two} = {result:.2f}")
    exit()
elif symbol_operation == "%":
    result = num_one % num_two
    print(f"{num_one} % {num_two} = {result}")
    exit()
print(f"{num_one} {symbol_operation} {num_two} = {result} - {result_check_up}")
