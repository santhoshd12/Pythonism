# class linkedlist:
#     def __init__(self, value,next=None):
#         self.value = value
#         self.next = next


# n1 = linkedlist(1)
# n2 = linkedlist(2)
# n3 = linkedlist(3)
# n4 = linkedlist(4)

# n1.next=n2
# n2.next=n3
# n3.next = n4

# ptr = n1
# while True:
#     print (ptr.value, end=" ")
#     if ptr.next==None:
#         print("None")
#         break
#     ptr = ptr.next


class node:
    def __init__(self,value):
        self.value = value
        self.next =  None

class linkedlist:
    def __init__(self,head=None):
        self.head = head
    
    def __len__(self):
        c=0
        last = self.head
        while last is not None:
            c+=1
            last=last.next

        print(c)
        
    def get(self,index):
        last = self.head
        if last is None:
            raise ValueError("invalid")
        for i in range(index):
            if last.next is None:
                raise ValueError("invalid")
            last =  last.next
        print(last.value)

    def appendv(self,value):
        Node = node(value)
        if self.head is None:
            self.head=Node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=Node

    def prepend(self,value):
        fn = node(value)
        fn.next=self.head
        self.head=fn

    def __prep__(self):
        last = self.head
        rs = f"[{last.value}"
        while last.next :
            last = last.next
            rs += f", {last.value}"
            
        rs+="]"
        print(rs)
    
    def insertval(self,value,index):
        if index==0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("invalid")

            else:
                last=self.head
                for i in range(index-1):
                    if last.next is None:
                        print("invalid")
                    last=last.next
                newnode=node(value)
                newnode.next=last.next
                last.next=newnode

    def __contain__(self,val):
        last = self.head
        while last.next is not None:
            if last.value==val:
                print('yes')
                return 
            last=last.next
        print("no")
        return 

    def delete(self,value):
        last = self.head
        if last is not None:
            
            if last.value==value:
                self.head = last.next

            else:
                while last.next:
                    if last.next.value==value:
                        last.next = last.next.next
                        break
                    last = last.next

    def pop(self, index):
        last = self.head
        if last is None:
            raise ValueError("invalid")
        else:
            for i in range(index-1):
                if last.next is None:
                    raise ValueError("invalid")
                last = last.next
            if last.next is None:
                last.value = None
            else:
                last.next = last.next.next

    def printlist(self):
        curr = self.head
        while curr is not None: 
            print(curr.value,end="->")
            curr=curr.next
        print("None")

# ll = linkedlist()

# ll.appendv(3)
# ll.printlist()

# ll.prepend(1)
# ll.printlist()

# ll.appendv(5)
# ll.printlist()

# ll.appendv(7)
# ll.printlist()

# ll.insertval(10,2)
# ll.printlist()

# ll.insertval(50,0)
# ll.printlist()

# ll.insertval(34,5)
# ll.printlist()

# ll.__contain__(50)
        
# ll.__len__()

# ll.delete(10)
# ll.printlist()

# ll.pop(5)
# ll.printlist()

# ll.get(4)

# # ll.show()

# print(ll)

# print( 10 in ll)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()
