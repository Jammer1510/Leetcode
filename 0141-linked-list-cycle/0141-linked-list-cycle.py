# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nums = set()
        cur = head
        
        while cur:
            if cur in nums:
                return True
            nums.add(cur)
            cur = cur.next
        return False