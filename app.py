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


def main():
    # #ask if user wants to continue with number in file or start from another number
    # user_decision = input("Do you want to:\nCONTINUE going or try a NEW number: ")

    # if user_decision.upper() == "NEW":
    #     number = int(input("Enter a whole number: "))
        
    #     if number % 1 != 0:
    #         print("Invalid input. Please try again.")
    #         main()

    #     #clear contents
    #     file = open("collatz_data.txt", "w")
        
    #     while True:
    #         print(f"{number}: {collatz(number)}")
    #         #clear contents and write input,max,steps (number,return_collatz_max,collatz(number))
    #         file_data = f"input:{number},max:{return_collatz_max(number)},steps:{collatz(number)}"
    #         file.write(file_data)
    #         print(file.read())
    #         number += 1
    #     file.close()
            
    # elif user_decision.upper() == "CONTINUE":
    #     number = open("collatz_data.txt", "r").read()
    #     number.close()
    #     #continue processing from that number

    #     file = open("collatz_data.txt", "w")
    #     while True:
    #         print(f"{number}: {collatz(number)}")
    #         number += 1
    # else:
    #     print("Invalid input. Please try again.")
    #     main()

    user_input = int(input("Enter a number: "))

    for number in range(user_input, 0, -1):
        print(f"{number}: {collatz(number)}")


if __name__ == "__main__":
    main()
