# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l[int(len(l) / 2):]

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution.middleNode([1,2,3,4,5]))
    print(solution.middleNode([1,2,3,4,5,6]))
