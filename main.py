# Object arrays cannot be loaded when allow_pickle=False

import numpy as np

np.save('data.npy', np.array([[1, 2, 3], [4, 5, 6]], dtype=object))

arr = np.load('data.npy', allow_pickle=True)

# [[1 2 3]
#  [4 5 6]]
print(arr)