import numpy as np
import matplotlib.pyplot as plt

M = 1000
test_x = np.linspace(0, 4*np.pi, M)
test_y = np.zeros(test_x.size, dtype=complex)
for i in range(1, M+1):
    # y是 M 个不同幅度的正弦序列的叠加
    test_y += 4 * np.sin((2 * i - 1) * np.pi * test_x) / (np.pi*(2 * i - 1))
# test_y = np.array([test_x[t]*2 for t in range(test_x.size)])

fu_array = np.zeros((M, M), dtype=complex)
fu_array = np.array([[test_y[t]*np.exp(-1j*2*np.pi*u*t/M)
                      for t in range(test_y.size)] for u in range(test_y.size)])
FU = np.array([np.mean(fu_array[u])
               for u in range(M)])  # 正傅里叶变换这里通过求平均，相当于除以M了。
FU1 = FU.reshape((1, FU.size))
# print('fu_array===========================')
# print(fu_array)
print('FU1===========================')
print(FU1.shape)


# 逆变换
#y_new = NP_FFT.ifft(FU1)
fx_array = np.zeros((M, M), dtype=complex)
fx_array = np.array([[FU1[0, t]*np.exp(1j*2*np.pi*u*t/M)
                      for t in range(M)] for u in range(M)])
FX = np.array([np.sum(fx_array[t]) for t in range(M)])  # 逆变换这里只求和，不再除以M
FX1 = FX.reshape((1, FU.size))

print('======print(FX1)=====================')
print(FX1.shape)
print('===========================')

plt.figure(figsize=(12, 8))
plt.subplot(311)
plt.title('Origion')
plt.grid(linestyle=':')
plt.plot(test_x, test_y, label='y')  # y是
plt.legend()

plt.subplot(312)
plt.title('Inverse Signal')
plt.grid(linestyle=':')
plt.plot(test_x, FX1[0], label='y_new', color='orangered')  # y是ifft变换后的序列
plt.legend()
plt.tight_layout()
plt.show()
