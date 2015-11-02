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



def deleteDupLinkedList(head):
    currentNode = head
    dict = { currentNode.next = True}

    if currentNode.next == None:
        return head
    while currentNode.next != None or currentNode != None:
        if dict[currentNode.val] == True: 
            currentNode.next = currentNode.next.next
        else:
            dict[currentNode.val] = True
            currentNode = currentNode.next

def deleteDupLinkedList(head):
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

def betterDeleteDupLinkedList(head):
    # add a check 
    if head == None:
        return 
    elif head.next == None:
        return head

    current = head
    while current != None or current.next != None:
        if current == current.next:
            current.next = current.next.next
        else:
            current = current.next
