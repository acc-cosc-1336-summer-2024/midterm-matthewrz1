#add import

import question_c

def main():

    x = True
    string1 = str(input("Please enter a string: "))
    Ask_Exit = "N"

    while x == True:
        if x == True:
            rev_string = question_c.reverse_string(string1)
            print("Reverse of ", string1, "is: ", rev_string)
            Ask_Exit = input("Would you like to exit? Y or N: ")
            if Ask_Exit == "Y":
                print("You have exit")
                x = False
            elif Ask_Exit == "N":
                print("Staying in string function")
                string1 = str(input("Please enter a string: "))

main()
