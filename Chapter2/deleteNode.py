def deleteNode(head, node):
    if head == None:
        return "You can't delete from an empty linked list"

    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next

    else:
        #if the last element is going to be deleted
        node.value = None

    return head


    
