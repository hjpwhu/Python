from __future__ import print_function

import torch

x = torch.Tensor(5, 3)
print(x)
print(x.size())

x = torch.rand(5, 3)
print(x)

y = torch.rand(5, 3)
print(y)
print(x + y)
print(torch.add(x, y))

result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print(result)

y.add_(x)
print(y)

print(x)
print(x[:, 0])

a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

import numpy as np

a = np.ones(5)
print("test!")
print(a)
b = torch.from_numpy(a)
print(b)
np.add(a, 1, out=a)
print(a)
print(b)

if torch.cuda.is_available():
    print("gpu")
else:
    print("cpu")