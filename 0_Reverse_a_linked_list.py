class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr=head
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        head=prev
        return head
