num = 70
factorial = 1

if num < 0:
    print("Sorry cant do that on numbers below 0")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)