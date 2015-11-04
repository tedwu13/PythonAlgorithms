class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = None

def printLinkList(head):
    while head != None:
        print head.val
        head = head.next
        
