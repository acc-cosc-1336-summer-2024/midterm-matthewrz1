#add import

import question_d

def main():
    x = True
    num = int(input("Enter a number: "))
    Ask_Exit = "N"

    while x == True:
        if question_d.is_prime(num) == True:
            print(num, "is a prime number,", question_d.is_prime(num))
            Ask_Exit = input("Would you like to exit? Y or N: ")
            if Ask_Exit == "Y":
                print("You have exit")
                exit()
            elif Ask_Exit == "N":
                print("Staying in function")
                num = int(input("Enter another number: "))

        elif question_d.is_prime(num) == False:
            print(num, "is not a prime number,", question_d.is_prime(num))
            Ask_Exit = input("Would you like to exit? Y or N: ")
            if Ask_Exit == "Y":
                print("You have exit")
                exit()
            elif Ask_Exit == "N":
                print("Staying in function")
                num = int(input("Enter another number: "))


main()
