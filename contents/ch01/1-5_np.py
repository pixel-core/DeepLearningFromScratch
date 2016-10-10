import numpy as np

print('1.5　NumPy')
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print('1.5.3　NumPyの算術計算')
print(x + y) # [ 3.  6.  9.]

print(x - y) # [-1. -2. -3.]

print(x * y) # [  2.   8.  18.]

print(x / y) # [ 0.5  0.5  0.5]

print(x / 2) # [ 0.5  1.   1.5]

print('1.5.4　NumPyのN次元配列')
A = np.array(
    [[1, 2],
    [3, 4]]
)
B = np.array(
    [[3, 0],
    [0, 6]]
)

print(A)
'''
[[1 2]
 [3 4]]
 '''

print(A.shape) # (2, 2)
print(A.dtype) # int64

print(A + B)
'''
[[ 4  2]
 [ 3 10]]
 '''

print(A * B)
'''
[[ 3  0]
 [ 0 24]]
'''

print(A * 10)
'''
[[10 20]
 [30 40]]
'''


print('1.5.5　ブロードキャスト')
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)
'''
[[10 40]
 [30 80]]
'''

print('1.5.6　要素へのアクセス')
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
'''
[[51 55]
 [14 19]
 [ 0  4]]
'''
print(X[0])    # [51 55]
print(X[0][1]) # 55

for row in X:
    print(row)
'''
[51 55]
[14 19]
[0 4]
'''

X = X.flatten()
print(X)                      # [51 55 14 19  0  4]
print(X[np.array([0, 2, 4])]) # [51 14  0]

print(X > 15)    # [ True  True False  True False False]
print(X[X > 15]) # [51 55 19]
