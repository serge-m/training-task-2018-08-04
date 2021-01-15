#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# In[2]:


import torch

torch.manual_seed(123)

true_w = 1.5
true_b = -2.

x = torch.linspace(-3, 3, 10)
x

# In[3]:


true_y = x * true_w + true_b
y = true_y + torch.normal(0., 0.2, x.size())
y
plt.plot(x, true_y)
plt.scatter(x, y)
plt.title("input data. real and with noise")
plt.show()

# In[4]:


w = torch.tensor(10., requires_grad=True)
b = torch.tensor(10., requires_grad=True)

lr = 0.01


def loss_fn(y, y_hat):
    return (y_hat - y).pow(2).sum()


history_w = []
history_b = []
history_loss = []
verbose = False

for epoch in range(50):
    y_hat = w * x + b
    loss = loss_fn(y, y_hat)
    loss.backward()

    w.data = w.data - lr * w.grad.data
    b.data = b.data - lr * b.grad.data

    w.grad.data.zero_()
    b.grad.data.zero_()

    if verbose:
        print(f"w: {w}")
        print(f"b: {b}")

    history_w.append(w.item())
    history_b.append(b.item())
    history_loss.append(loss.item())

print(f"w: {w} vs true {true_w}")
print(f"b: {b} vs true {true_b}")

# In[5]:


for i, (hw, hb, hl) in enumerate(zip(history_w, history_b, history_loss)):
    if i % 5 != 0:
        continue
    plt.figure()
    plt.plot(x, true_w * x + true_b, label="true")
    plt.scatter(x, y, label="noise")
    plt.ylim(min(y), max(y))
    plt.plot(x, hw * x + hb, label="prediction")
    plt.title(f"{loss}")
    plt.show()
