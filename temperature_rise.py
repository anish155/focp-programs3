def temperature():
    print("Enter six Celsius values:")
    number = float(input("Enter first Celsius: "))
    number1 = float(input("Enter second Celsius: "))
    number2 = float(input("Enter third Celsius: "))
    number3 = float(input("Enter fourth Celsius: "))
    number4 = float(input("Enter fifth Celsius: "))
    number5 = float(input("Enter sixth Celsius: "))
    return number, number1, number2, number3, number4, number5

def fahrenheit_convert(celsius_values):
    return [(celsius * 9 / 5) + 32 for celsius in celsius_values]

def min_max_mean(values):
    minimum = min(values)
    maximum = max(values)
    mean = sum(values) / len(values)
    return minimum, maximum, mean


celsius_values = temperature()
fahrenheit_values = fahrenheit_convert(celsius_values)
minimum, maximum, mean = min_max_mean(fahrenheit_values)

print(f"Fahrenheit values: {fahrenheit_values}")
print(f"Minimum Fahrenheit: {minimum}F")
print(f"Maximum Fahrenheit: {maximum}F")
print(f"Mean Fahrenheit: {mean}F")

