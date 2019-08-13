#create a function to get a integer value of string
def getinteger(inputString) :
    output_integer = 0

    #check for negative sign
    if inputString[0] == '-' : 
        startwith = 1
        is_negative = True
    else:
        startwith = 0
        is_negative = False

    for i in range( startwith, len(inputString)) :
        place = 10 ** (len(inputString) - (i+1))
        digit = ord(inputString[i]) - ord('0')
        output_integer += place * digit

    if is_negative :
        return -1 * output_integer
    else:
        return output_integer


#driver code :
s = '-554'
print (s) #given type <str>
print (type(s))
x = getinteger(s)
print (x)
print (type(x)) #change to <int>
