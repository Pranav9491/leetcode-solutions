# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):

        temp=head
        d={}
        while temp:
            if temp not in d:
                d[temp]=1
                temp=temp.next
            else:
                return temp
        return None

        """slow,fast=head,head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None"""