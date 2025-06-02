import numpy as np

_bytes = np.fromfile("file.txt", dtype='uint8')
print("bytes: ", _bytes)
''' output

bytes:  [ 72 101 108 108 111  32 119 111 114 108 100]

'''



bits = np.unpackbits(_bytes)
print("\nbits: ", bits)
''' output

bits: [0 1 0 0 1 0 0 0 0 1 1 0 0 1 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 1 0 1
 1 1 1 0 0 1 0 0 0 0 0 0 1 1 1 0 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 0 0 1 0 0 1
 1 0 1 1 0 0 0 1 1 0 0 1 0 0]

'''



rows = 10
columns = 8
numpy1D = np.array( [0,1,1,0,0,1,0,1,1,1] ) # 10 bits
numpy2D = np.zeros( (rows, columns) ) 

numpy2D[:, 2] = numpy1D
numpy2D[:5, 7] = [1,1,0,1,1]
numpy2D[2:, 6] = [1,0,1,0,0,1,1,1] 
print("\ntransposed array: \n", numpy2D)
''' output

transposed array: 
[[0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 1. 0. 0. 0. 0. 1.]
 [0. 0. 1. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0. 0. 1. 1.]
 [0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 1. 0.]
 [0. 0. 1. 0. 0. 0. 1. 0.]
 [0. 0. 1. 0. 0. 0. 1. 0.]]

'''


numpy1D = np.concatenate(numpy2D)
print("\nconcatenated: ", numpy1D)
''' output

concatenated: [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 1. 0.
 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 1. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 1. 0. 0. 0. 1. 0. 0. 0. 1. 0.
 0. 0. 1. 0. 0. 0. 1. 0.]

'''