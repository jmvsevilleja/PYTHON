# Input divisible by 3 Fizz
# Input divisible by 5 Buzz
# Input divisible by 3 and 5 FizzBuzz
# Else return input itself


def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    if(input % 3 == 0):
        return "Fizz"
    if(input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz(15))
