#write functions here, don't add input('') statements here!

def get_bonus_pay(sales):

    if sales >= 0 and sales < 500:
        bonus_pay = sales*.05
        return bonus_pay
    
    elif sales >= 500 and sales < 1000:
        bonus_pay = sales*.06
        return bonus_pay
    
    elif sales >= 1000 and sales < 1500:
        bonus_pay = sales*.07

    elif sales >= 1500 and sales <=1999:
        bonus_pay = sales*.08

    else:
        bonus_pay = "Invalid arguments"
    
    return bonus_pay