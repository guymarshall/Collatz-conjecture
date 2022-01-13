import matplotlib.pyplot as plt
import numpy as np

def collatz(number):
    counter = 0
    while number > 1:
        counter += 1

        if number % 2 != 0:
            number = (number * 3) + 1
        else:
            number /= 2

    return counter


def return_collatz_max(number):
    max = 0
    while number > 1:
        if number % 2 != 0:
            number = (number * 3) + 1
        else:
            number /= 2

        if number > max:
            max = number

    return max


def return_collatz_array(number):
    answers = [number]
    while number > 1:
        if number % 2 != 0:
            number = (number * 3) + 1
        else:
            number /= 2

        answers.append(number)

    return answers


def main():
    collatz_input = int(input("Enter a whole number: "))
    user_decision = input("Calculate MAX or ALL? ")

    if user_decision.upper() == "MAX":
        y_points = np.array(return_collatz_array(collatz_input))

        plt.plot(y_points, linestyle = "dotted")
        plt.show()

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
