#Reverse a linked list

def reverse(head):
    prev = None

    while current != None:
        current = head
        next = current.next
        current.next = prev
        prev = None
    return head


