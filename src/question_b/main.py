#add import

import question_b

def main():

    sales = int(input("Please enter sales amount: "))
    bonus_pay = question_b.get_bonus_pay(sales)

    if bonus_pay != "Invalid arguments":
        print("Your bonus pay is: ", bonus_pay)

    else:
        print(bonus_pay)

main()

