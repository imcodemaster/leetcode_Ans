#valid Prenthese
openlist = ['(','{','[']
closelist = [')', '}', ']']

#function to check validity
def check (string):
    stack = []
    for i in string :
        print('i in string : ' , i) #command just to check and understand what happen 
        if i in openlist :
            print('i in openlist : ', i) #command just to check and understand what happen
            stack.append(i)
            print('append in stack : ' , stack) #command just to check and understand what happen
             
        elif i in closelist :
            pos = closelist.index(i)
            print ('pos : ' , pos) #command just to check and understand what happen
            
            #lenght of stack after appending string is more then 0
            #and pos in openlist is strickly
            #equal to last element in stack (last in first out) 
            if len(stack) > 0 and openlist [pos] == stack[len(stack)-1] :
                print('stack to check : ' , stack) #command just to check and understand what happen

                print('last element : ' , stack[len(stack)-1])
                stack.pop() #pop it 
                print('stack after poping : ' , stack) #command just to check and understand what happen
            else:
                return 'Unbalanced'
        if len(stack) == 0 :
            return 'Balanced'


#Driver Code :
string = '({]})'
print (string , ' - ' , check(string))
                        
            
            
