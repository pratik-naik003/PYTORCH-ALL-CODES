# the tensor is the fundamental data  structure present in pytorch
import torch 
scaler=torch.tensor(7);
print(scaler)

# vector (1D tensor)
vector=torch.tensor([10,29,38,49])
print(vector)

# matrix 2D tensor
matrix=torch.tensor([[1,45,545],
                     [57,49,39]])
print(matrix)

#dimension of tensor
print(vector.ndim)
print(matrix.ndim)

#finding  the shape of tensor
print(vector.shape)
print(matrix.shape)

#number of elements in the  tensor
print(vector.numel())
print(matrix.numel())

#getting the data types of  any tensor
print(vector.dtype)
print(matrix.dtype)

# geeting the device name of the tensor
print(vector.device)
print(matrix.device)

