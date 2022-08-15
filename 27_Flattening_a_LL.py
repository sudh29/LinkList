def flatten(root):
    #Your code here
    temp=[]
    curr=root
    while curr:
        temp.append(curr.data)
        b=curr.bottom
        while b:
            temp.append(b.data)
            b=b.bottom
        curr=curr.next
    temp.sort()
    res=root
    prev=None
    for i in temp:
        if res:
            res.data=i
            prev=res
            res=res.bottom
        else:
            temp=Node(i)
            prev.bottom=temp
            prev=prev.bottom
    return root
