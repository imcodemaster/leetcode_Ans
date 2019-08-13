# convert integer to string representation

def getstring (inputint):

    if inputint < 0 : #checking for negative integer
        is_negative = True
        inputint *= -1 #making it positive
    else :
        is_negative = False

    outputstr = []
    while inputint > 0 :
        outputstr.append(chr(ord('0') + inputint % 10 ))
        inputint //= 10
    outputstr = outputstr[:: -1] #reversing <str> in list

    outputstr = ''.join(outputstr) #joing all <str> without space in b/w them.

    #if its negative int then :
    if is_negative :
        return '-' + outputstr
    else:
        return outputstr

#Driver code :

inputint = -123
print (inputint) #given <int>
print(type(inputint))
print (getstring(inputint)) #calling function
print (type(getstring(inputint))) #convert <int> to <str>

#task completed 

