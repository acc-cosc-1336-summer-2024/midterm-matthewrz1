#write functions here, don't add input('') statements here!

def is_prime(num):

    if int(num) == 1:
        return False
    elif int(num) != 1:
        y = 0
        for x in range(1,num+1):
            if num % x == 0:
                y = y + 1
            else:
                y = y
        if y > 2:
            return False
        elif y <= 2:
            return True
