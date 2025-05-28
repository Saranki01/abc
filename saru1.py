class Node:
    def __init__ (self , data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def _inset_at_Beginning(self,newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode


ll = LinkedList()
ll.head = Node("Toyota")
l2 = Node("BMW") 
l3 = Node("Audi")
l4= Node("Lambogini")
ll.head.next = l2
l2.next = l3
l3.next = l4

ll.listprint()
print("")
ll._inset_at_Beginning("Benz")
ll.listprint()
ll._inset_at_Beginning("chr")
print("")
ll.listprint()