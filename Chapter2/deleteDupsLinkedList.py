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


# use a dictionary to keep track of all the elements in the linked lists

def deleteDupLinkedList(head):
    currentNode = head
    while currentNode != None or currentNode.next!= None:
        runnerNode = currentNode
        while runnerNode.next != None:
            if runnerNode == runnerNode.next:
                runnerNode = runnerNode.next.next
            else:
                runnerNode = runnerNode.next
    return head
    
