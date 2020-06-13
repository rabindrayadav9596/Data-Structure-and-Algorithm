'''push current node and go to left child.
Do this till left child == null

Break condition

pop node

print that node

go to right child of that node

iterative inorder traversal

while true:
    while p:
        push p
        p = p.left

    if( stackEmpty()):
        break

    p = pop()
    print (p.data)
    p = p.right

iterative pre-order traversal

while true:
    while p:
        print and push p
        p = p.left

    if(stackEmpty()):
        break
    p = pop()
    p = p.right
'''
