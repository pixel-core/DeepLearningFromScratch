import numpy as np

print('2.3.2　重みとバイアスの導入')
x = np.array([0, 1])     # 入力
w = np.array([0.5, 0.5]) # 重み
b = -0.7                 # バイアス

print(w*x)             # [ 0.   0.5]
print(np.sum(w*x))     # 0.5
print(np.sum(w*x) + b) # -0.2

print('2.3.3　重みとバイアスによる実装')
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
