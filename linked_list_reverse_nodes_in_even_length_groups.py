"""
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned 
to non-empty groups whose lengths form the sequence of 
the natural numbers (1, 2, 3, 4, ...). The length of a 
group is the number of nodes assigned to it. In other words,
    The 1st node is assigned to the first group.
    The 2nd and the 3rd nodes are assigned to the second 
        group.
    The 4th, 5th, and 6th nodes are assigned to the third 
        group, and so on.

Note that the length of the last group may be less than or 
equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and 
return the head of the modified linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=ListNode):
        self.head = head

    def createList(self, inputList: list) -> ListNode:
        for i, num in enumerate(inputList):
            if i == 0:
                head = ListNode(num)
                node = head
            else:
                node.next = ListNode(num)
                node = node.next
        return head

    def printList(self, head: ListNode):
        node = head
        output = ""
        while node:
            output += " " + str(node.val)
            node = node.next

        print(f"list:{output}")


class Solution:
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        group_count = 0
        count = 0
        type = "odd"
        curr = head

        while curr:
            if count == group_count or curr.next is None:
                if count % 2 == 0:
                    type = "even"
                else:
                    type = "odd"
                count = 0

            count += 1

            print(f"grp: {group_count}, cnt: {
                  count}, val: {curr.val}, type: {type}")

            curr = curr.next


sol = Solution()
ll = LinkedList()

# ex 0: Output:
head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
head = ll.createList(head)
head = sol.reverseEvenLengthGroups(head)
ll.printList(head)

# # ex 1: Output: [5,6,2,3,9,1,4,8,3,7]
# head = [5, 2, 6, 3, 9, 1, 7, 3, 8, 4]
# head = ll.createList(head)
# head = sol.reverseEvenLengthGroups(head)
# ll.printList(head)

# # ex 1: Output: [5,6,2,3,9,1,4,8,3,7]
# head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# head = ll.createList(head)
# head = sol.reverseEvenLengthGroups(head)
# ll.printList(head)
