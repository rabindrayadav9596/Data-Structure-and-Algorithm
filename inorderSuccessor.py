'''case I

if the node has a right subtree,
then find the lease value node from
that right subtree

if(p.right != None):
    temp = p.right
    while temp.left != None:
        temp = temp.left
    print (temp)

case II
if the node does not have right subtree,
search that p from root, the node from where
we take the last left is the answer

s = root
while s.data != p.data:
    if p.data <= s.data:
        store = s
        s = s.left
    else:
        s = s.right
    print(store)
'''
