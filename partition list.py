class Solution(object):
    def partition(self, head, x):
      

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next
