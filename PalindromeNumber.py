#palindrome number
def Palindromenumber (x) :
    if x < 0  and x != 0 and x % 10 == 0 : #check for 0 , -ve, or remainder
        return False

    else :
        reverse = 0
        original = x
        while x != 0 :
            reverse = reverse * 10 + x % 10 #seperate last one and get its place vlaue
            x //= 10
        print (reverse)
        return reverse == original #check for same or not 
            
#driver code :
x = 123
print (Palindromenumber(x))

x = 121
print (Palindromenumber (x))

