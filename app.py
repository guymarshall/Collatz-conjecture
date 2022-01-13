def collatz(number):
    counter = 0
    while number > 1:
        counter += 1

        if number % 2 != 0:
            number = (number * 3) + 1
        else:
            number /= 2

    return counter


def main():
    collatz_input = int(input("Enter a whole number: "))
    user_decision = input("Calculate SINGLE or ALL? ")

    if user_decision.upper() == "SINGLE":
        print(f"{collatz_input}: {collatz(collatz_input)}")
    elif user_decision.upper() == "ALL":
        counter = 1
        while counter <= collatz_input:
            print(f"{counter}: {collatz(counter)}")
            counter += 1
    else:
        print("Invalid input. Please try again.")
        main()

if __name__ == "__main__":
    main()
