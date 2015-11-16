def deleteDupLinkedList(head):
    currentNode = head
    dict = { currentNode.val: True}

    if currentNode.next == None:
        return head
    while currentNode.next != None or currentNode != None:
        if dict[currentNode.next.val]:
            currentNode.next = currentNode.next.next
        else:
            dict[currentNode.next.val] = True
            currentNode = currentNode.next



def removeDuplicate(head):
    if head == None:
        return -1
    current = head
    dict = {}
    
    while current.next != None and current != None:
        if current.next.val in dict:
            if current.next.next == None:
                current.next = None
            else:    
                current.next = current.next.next
        else:
            dict[current.next.val] = True
    
        current = current.next
    return head


def deleteDupLinkedList(head):
    # add a check 
    if head == None:
        return 
    elif head.next == None:
        return head
    #if you cannot use a dictionary to keep track of the linked lists
    current = head
    while current != None or current.next != None:
        runner = current
        while runner.next != None:
            if runner == runner.next:
                runner.next = runner.next.next
            else:
                runner = runner.next
    return head

