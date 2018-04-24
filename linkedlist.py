class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class CreateList: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    
    def insert(self,head,data):
        if head == None:
            n = Node(data)
            head = n
        else:               
            head = self.reverse(head)           
            n = Node(data)
            n.next = head
            head = n        
            head = self.reverse(head)
        return head
    
    def reverse(self,head):
        rev = None   
        current = head
        while current:
            next =  current.next
            current.next = rev
            rev = current
            current = next      
        return rev

if __name__ == "__main__":
    mylist= CreateList()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head); 
