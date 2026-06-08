class Solution:

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def compute(self, head):

        head = self.reverse(head)

        max_node = head
        curr = head

        while curr and curr.next:

            if curr.next.data < max_node.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_node = curr

        return self.reverse(head)