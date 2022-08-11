class Solution:
    def divide(self, N, head):
        # code here
        curr=head
        temp=[]
        while curr:
            temp.append(curr.data)
            curr=curr.next
        temp1=[]
        temp2=[]
        for i in temp:
            if i%2==0:
                temp1.append(i)
            else:
                temp2.append(i)
        temp=temp1+temp2
        curr=head
        for i in temp:
            curr.data=i
            curr=curr.next
        return head
