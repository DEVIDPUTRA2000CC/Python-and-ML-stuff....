import numpy as np
a= np.array([])
we can multiplay arrya matrix by just a*b
a=np.array([
    [
    [[2, 3], [4, 6]],
                     [[1, 3], [3, 4]], 
                                      [[4, 5], [3, 5]]
           ],
    [
    [[2, 3], [4, 6]],
                     [[1, 3], [3, 4]], 
                                      [[4, 5], [3, 5]]
           ]
])
print("No. of dimention-> ", a.ndim)
print("shape-> ", a.shape)
print("length of shape-> ", len(a.shape))
print("size-> ", a.size)
  # here our 4th diention has 2 elements 
  # Element -> 1 [
   # [[2, 3], [4, 6]],
    #[[1, 3], [3, 4]], 
     # [[4, 5], [3, 5]]
      #     ],
    # Element ->2 [
   # [[2, 3], [4, 6]],
    #                 [[1, 3], [3, 4]], 
     #                                 [[4, 5], [3, 5]]
      #     ] 
 # now in each dimention there are 3 elements 
#[[2, 3], [4, 6]],
#[[1, 3], [3, 4]], 
#[[4, 5], [3, 5]]
# and in each there is 2 
#[[2, 3], [4, 6]]

# 2 particular elements
# like [2, 3]
# so thats why shape is (2, 3, 2, 2).

OUTPUT->
No. of dimention->  4
shape->  (2, 3, 2, 2)
length of shape->  4
size->  24
