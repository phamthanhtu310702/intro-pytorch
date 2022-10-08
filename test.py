import torch as pt
from torch.utils.data import TensorDataset
pt.manual_seed(0)
X = pt.linspace(-5, 5, 100)
y = 2 * X + pt.randn(len(X))
train_ds = TensorDataset(y, X)
