
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # p = head
        # s = ""
        # while p:
        #     s += " " + str(p.val)
        #     p = p.next
        # print(s)

        if not head:
           return None
        elif not head.next:
            return head
        slow, fast = head, head.next
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        s1, s2 = head, slow.next
        slow.next = None
        s1 = self.sortList(s1)
        s2 = self.sortList(s2)
        new_head = ListNode()
        p = new_head
        while s1 and s2:
            if s1.val < s2.val:
                p.next = s1
                s1 = s1.next
            else:
                p.next = s2
                s2 = s2.next
            p = p.next
        
        while s1:
            p.next = s1
            p = p.next
            s1 = s1.next

        while s2:
            p.next = s2
            p = p.next
            s2 = s2.next
        
        p.next = None
        return new_head.next

sol = Solution()
head = ListNode(4)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(1)
h = sol.sortList(head)

p = h
s = ""
while p:
    s += " " + str(p.val)
    p = p.next
print(s)