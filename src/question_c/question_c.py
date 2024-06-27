#write functions here, don't add input('') statements here!

def reverse_string(string1):

    len_string = len(string1)-1
    rev_string = ''

    while len_string >= 0:

        rev_string = rev_string + string1[len_string]
        
        len_string = len_string - 1
    
    return rev_string

