class Solution:
    def reverse(self,head, k):
        # Code here
        curr=head
        temp=[]
        while curr:
            temp.append(curr.data)
            curr=curr.next
        for i in range(0,len(temp),k):
            if i+k<=len(temp):
                val=temp[i:i+k]
                temp[i:i+k]=val[::-1]
            else:
                val=temp[i:]
                temp[i:]=val[::-1]
        curr=head       
        for i in range(len(temp)):
            curr.data=temp[i]
            curr=curr.next

        return head
