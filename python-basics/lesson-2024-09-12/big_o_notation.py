
# '''
# Algorithmic Analysis: Big O notation

# O(1)
# O(n)
# O(log(n))
# O(nlog(n))
# O(n^2)
# O(2^n)

# '''

# import numpy as np

# n = np.linspace(1, 300, 300)

# # print(n)

# o_1 = np.ones_like(n)

# # print(o_1)

# o_n = n

# # print(o_n)

# o_log_n = np.log(n)

# # print(o_log_n)

# o_n_log_n = n * np.log(n)


# # --> n(np.log(n)) --> wrong syntax

# # copy = n(np.log(n)) --> wrong syntax

# # print(copy)

# # print(o_n_log_n)

# o_n_2 = n**2


# # print(o_n_2)

# o_2_n = 2**n

# # print(o_2_n)


# import matplotlib.pyplot as plt


# plt.figure(figsize=(20, 16))

# plt.plot(n, o_1, label='O(1)')


# plt.legend()

# plt.show()

import numpy as np

n = np.linspace(1, 300, 300)

# print(n)

o_1 = np.ones_like(n)

# print(o_1)

o_n = n

# print(o_n)

o_log_n = np.log(n)

# print(o_log_n)

o_n_log_n = n * np.log(n)


# --> n(np.log(n)) --> wrong syntax

# copy = n(np.log(n)) --> wrong syntax

# print(copy)

# print(o_n_log_n)

o_n_2 = n**2


# print(o_n_2)

o_2_n = 2**n

# print(o_2_n)


import matplotlib.pyplot as plt


plt.figure(figsize=(20, 16), dpi=300)

plt.plot(n, o_1, label='O(1)')
plt.plot(n, o_n, label='O(n)')
plt.plot(n, o_log_n, label='O(log(n))')
plt.plot(n, o_n_log_n, label='O(nlog(n))')
plt.plot(n, o_n_2, label='O(n^2)')
plt.plot(n, o_2_n, label='O(2^n)')


plt.xlabel('Input data size')
plt.ylabel('Operations / Time')
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.legend()
plt.show()

# Alt+Z