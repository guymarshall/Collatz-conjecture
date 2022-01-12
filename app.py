import math


def isPrimeNumber(number):
    ceiling_root = math.ceil(math.sqrt(number));
    if ceiling_root >= number:
        ceiling_root = number - 1

    counter = 2
    while counter <= ceiling_root:
        if number % counter == 0:
            return False
        counter += 1
    return True


def calculateFactorial(number):
    result = 1
    counter = 2
    if number > 1:
        while counter <= number < 1:
            result = result * counter
            counter += 1
    return result;


def calculate(number):
    counter = 0
    while number > 0:
        counter += 1

        if number % 2 != 0:
            number = ((number * 3) + 1) / 2
        else:
            number /= 2

    return counter


def main():
    message = """
0 - PrimeNumber
1 - Factorial
2 - CollatzConjecture
Choose method: """
    method_choice = int(input(message))

    if method_choice == 0:
        prime_input = int(input("Number: "))

        counter = 2
        while counter <= prime_input:
            is_prime = isPrimeNumber(counter)
            if is_prime:
                print(f"{counter} is a prime number")
            counter += 1
    elif method_choice == 1:
        factorial_input = int(input("Enter an integer: "))
        print(f"{factorial_input}! = {calculateFactorial(factorial_input)}")
    elif method_choice == 2:
        collatz_input = int(input("Enter a whole number: "))
        user_decision = input("Calculate SINGLE or ALL? ")

        if user_decision.upper() == "SINGLE":
            print(f"{collatz_input}: {calculate(collatz_input)}")
        else:
            counter = 1
            while counter <= collatz_input:
                print(f"{counter}: {calculate(counter)}")
            counter += 1
    else:
        print(f"{method_choice} is invalid. Please try again.")

if __name__ == "__main__":
    main()



# FACTORIAL ALWAYS RETURNS 1 FOR SOME REASON
# COLLATZ HAS INFINITE LOOP WITHOUT PRINTING
