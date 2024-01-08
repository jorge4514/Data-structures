class LinkedList:
    def __init__ (self, value=0, next=None):
        self.value = value
        self.next = next

def ListMax(head):
    if(head == None):
        return None
    #cogemos el siguiente
    current_node = head.next
    #el actual es el mas grande
    current_max = head.value

    while current_node is not None:
        if(current_node.value > current_max):
            print(current_node.value)
            current_max = current_node.value
        current_node = current_node.next
    return current_max

head = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, None))))

max = ListMax(head)

print(max)