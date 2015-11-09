class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def printLinkList(head):
    while head != None:
        print head.val
        head = head.next
        
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

# def removeDuplicate2(head):
    
#     if head == None:
#         return -1
#     current = head
#     while current.next != None:
        

print "before", printLinkList(node1)
print "removing duplicates", removeDuplicate(node1)
print "after", printLinkList(node1)