# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head

        #gets to the last node
        while currentNode:
            tempNode = currentNode.next
            currentNode.next = prevNode #reverse 
            prevNode = currentNode
            currentNode = tempNode #advance to next
        
        return prevNode