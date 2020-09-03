# Program to evaluate whether a number is perfect

number_str = input("Please enter a number to check: ")
number = int(number_str)

# find a divisor and sum the divisors
divisor = 1
sum_of_divisors = 0
while divisor < number:
    if number % divisor == 0:    # divisor evenly divides the number
        sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1

# classify the result
if number == sum_of_divisors:
    print(number,"is perfect")
else:
    print(number,"is not perfect")