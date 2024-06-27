#add import

import question_a

def main():

    x = True
    value = int(input("Please enter your land value: "))
    Ask_Exit = "N"

    while x == True:
        if value >= 0:
            assessment_value = question_a.get_assessment_value(value)
            property_tax = question_a.get_tax_assessed(assessment_value)
            print("assessment value of", value, "is: ", assessment_value)
            print("tax assessed is: ", property_tax)
            Ask_Exit = input("Would you like to exit? Y or N: ")
            if Ask_Exit == "Y":
                print("You have exit")
                exit()
            elif Ask_Exit == "N":
                print("Asking for new property value")
                value = int(input("Please enter your land value: "))
        elif value < 0:
            value = int(input("Value not recognized, please enter land value: "))

main()








