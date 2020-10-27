import torch

num_steps = 100


def loss_fn(val, var):
    return (val - var).pow(2)


"""
X = [0 0] 

W [0.1 -0.1]
[0.01 -0.01]
W_b [0 0]

Target
[10, 10] 


loss = (10 - var)
grad = dloss / dvar = -1

lr = 1
var = var - lr * grad 

"""


def converge_variable_to_a_value():
    step = 0.1
    val = torch.tensor([10.])
    var = torch.tensor([0.], requires_grad=True)

    for i in range(num_steps):
        if var.grad is not None:
            var.grad.data.zero_()
        loss = loss_fn(val, var)
        loss.backward()
        with torch.no_grad():
            var -= step * var.grad.data


def test_main():
    converge_variable_to_a_value()


if __name__ == '__main__':
    converge_variable_to_a_value()
