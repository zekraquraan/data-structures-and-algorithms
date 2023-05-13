class Node : #value next
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class LinkedList:
    def __init__(self,head=None):
        self.head = head



    def insert (self, value) : 
         # insert vs append 
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node


    
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        if not self.head:
            return "NULL"
        
        current = self.head
        result = ""
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result

         





