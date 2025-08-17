first_value = input("Enter the first value: ")
second_value = input("Enter the second value: ")

operator = input("Enter the operator (+, -, *, /): ")
if operator == '+':
    result = float(first_value) + float(second_value)
    print(first_value + " + " + second_value + " = " + str(int(result)))
elif operator == '-':
    result = float(first_value) - float(second_value)
    print(first_value + " - " + second_value + " = " + str(result))
elif operator == '*':
    result = float(first_value) * float(second_value)
    print(first_value + "*" + second_value + "=" + str(result))
elif operator == '/':
    if float(second_value) != 0:
        result = float(first_value) / float(second_value)
        print(first_value + " / " + second_value + " = " + str(result))
    else:
        result = "Error: Division by zero is not allowed."
        print(result)
else:
    result = "Error: Invalid operator."
    print(result)