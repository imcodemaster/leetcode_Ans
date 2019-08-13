#Creating Node
class Node :
    def __init__ (self, data):
        self.data = data
        self.next = None

#creating Linked list
class LinkedList :
    def __init__ (self) : #constructor 
        self.head = None
        self.lastNode = None

    def append (self, data) : #method to Append
        if self.lastNode is None :
            self.head = Node(data)
            self.lastNode = self.head
        else:
            self.lastnode.next = Node(data)

    def Print( self) : #method to print linked list
        current = self.head
        while current is not None :
            print (current.data , end = ' ' )
            current = current.next

#method to add two linked list :
def addtwolinkedlist (llist1, llist2) :
    sumlist = LinkedList()
    current1 = llist1.head
    current2 = llist2.head
    while current1 and current2 :
        sum = current1.data + current2.data
        sumlist.append(sum)
        current1 = current1.next
        current2 = current2.next
        if current1 is None :
            while current2 :
                sumlist.append(current2.head)
                current2 = current2.next
        else :

            while current1 :
                sumlist.append(current1.head)
                current1  = current1.next
        return sumlist

#driver code  :

llist1 = LinkedList()
llist2 = LinkedList()

datalist = input('Enter number for first linked list : ').split()
for data in datalist :
    llist1.append(int(data))

datalist = input('Enter number for second linked list : ').split()
for data in datalist :
    llist2.append(int(data))

sumlist = addtwolinkedlist(llist1,llist2)
print (' the sum : ' , end = ' ')

sumlist.Print()



#task Complete ;)  

















                    












                    


        
        
