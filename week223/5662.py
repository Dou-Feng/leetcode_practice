from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def swap(node1, node2):
            if node2.next == node1:
                t = node1
                node1 = node2
                node2 = t
            if node1.next == node2:
                q = node2.next
                qnext = q.next
                p = node1.next
                node1.next = q
                q.next = p
                p.next = qnext
                return
            p, q = node1.next, node2.next
            pnext, qnext = p.next, q.next
            node1.next = q
            q.next = pnext
            node2.next = p
            p.next = qnext

        n = 0
        p = ListNode(0)
        new_head = p
        p.next = head
        nk_1 = None
        while p:
            if n == k-1 and nk_1 == None:
                nk_1 = p
            p = p.next
            n += 1
        # print(n, nk_1)
        p = new_head
        t = 0
        while t < n - k - 1:
            p = p.next
            t += 1
        if p != nk_1:
            swap(nk_1, p)

        return new_head.next





if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    s = sol.swapNodes(head, 2)
    while s:
        print(s.val)
        s = s.next