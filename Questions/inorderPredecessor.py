# case I

# if the node P has a left subtree,
# then jump to that left child and go 
# to the rightmost node (max value)

# if p.left != None:
#     temp = p.left
#     while temp.right != None:
#         temp = temp.right
#     print temp


# case II
# If the node P does not have left subtree, search that node 
# from the root, and the node from where we take the last right
# is the answer

# while p.data != s.data:
#     if (p.data>s.data):
#         store = s
#         s = s.right
#     else:
#         s = s.left
# print store