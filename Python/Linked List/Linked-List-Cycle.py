
#Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.

#Link: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #define both pointers at head
        slow = fast = head
        
        while slow and fast and fast.next:
            #slow pointer moves to one step ahead
            slow = slow.next 
            #fast pointer moves to two steps ahead
            fast = fast.next.next
            if slow == fast:
                return True
        return False
