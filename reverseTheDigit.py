def reverse_integer (x) :
    if x < 0 : 
        sign = -1
        x *= sign
    elif x > 0 :
        sign = 1
    while x :
        if x % 10 == 0 :
            x /= 10
        else :
            break

    #string Manipulation 
    x = str (x)
    lst = list(x)
    print ('original list with input :' ,  lst)
    lst.reverse()
    x = "".join(lst)
    print ('Reversed list with output : ' , lst)
    x = int(x)

    return sign * x

user = input('Enter number to reversed : ')
x = int(user) 
print (reverse_integer (x))

