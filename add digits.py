class Solution(object):
  #creating function
  def addDigits( num):
    while(num >= 10):
        temp = 0
        while(num > 0):
            temp += num % 10
            num /= 10
        num = temp
    return int(num)

#driver code
num  = 24
print (Solution.addDigits(num))
