'''
A node in a singly-linked list.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
Accepted 02/07/2021 11:32; runtime 28 ms, memory 14.2 MB.
'''


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        value = 0
        cursor = head
        while (cursor):
            if (cursor.next):
                value = cursor.val
                cursor.val = (cursor.next).val
                cursor.next.val = value
                # there is a sequential node, it is safe to advance one step.
                cursor = cursor.next
            # every two adjacent nodes are swapped; hence, we advance once more.
            cursor = cursor.next
        return head


'''
Prints a singly linked list from head to tail.
'''


def printSinglyLinkedList(head: ListNode):
    cursor = head
    while(cursor):
        print(f'[{cursor.val}]->', end='')
        cursor = cursor.next
    print('None')


# defines a singly linked list
# either
# node_03 = ListNode(3)
# or
node_03 = None
node_02 = ListNode(2, node_03)
node_01 = ListNode(1, node_02)
head = ListNode(0, node_01)
print('Before:')
printSinglyLinkedList(head)
print('\n')

#
Solution.swapPairs(None, head)

#
print('After:')
printSinglyLinkedList(head)
