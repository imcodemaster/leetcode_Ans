#valid Prenthese
openlist = ['(','{','[']
closelist = [')', '}', ']']

#function to check validity
def check (string):
    stack = []
    for i in string :
        print('i in string : ' , i)
        if i in openlist :
            print('i in openlist : ', i)
            stack.append(i)
            print('append in stack : ' , stack)
             
        elif i in closelist :
            pos = closelist.index(i)
            print ('pos : ' , pos)
            #lenght of stack after appending string is more then 0
            #and pos in openlist is strickly
            #equal to last element in stack (last in first out) 
            if len(stack) > 0 and openlist [pos] == stack[len(stack)-1] :
                print('stack to check : ' , stack)

                print('last element : ' , stack[len(stack)-1])
                stack.pop() #pop it 
                print('stack after poping : ' , stack)
            else:
                return 'Unbalanced'
        if len(stack) == 0 :
            return 'Balanced'


#Driver Code :
string = '({]})'
print (string , ' - ' , check(string))
                        
            
            
