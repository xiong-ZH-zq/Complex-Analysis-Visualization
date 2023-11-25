import matplotlib.pyplot as plt
import plotly.graph_objects as go
import torch    # 使用 torch 加速

def julia_set(Z, c, max_iter):
    """计算 Julia 集
    :param Z: 复数集
    :param c: 迭代常数
    :param max_iter: 最大迭代次数
    """
    out = torch.zeros_like(Z, dtype=torch.float32) + max_iter
    c = torch.zeros_like(Z)+c
    for n in range(max_iter):
        absZ = torch.abs(Z)
        Z[absZ>2] = 0
        c[absZ>2] = 0
        out[absZ>2] = n
        Z = Z*Z + c
    return out

xmin, xmax, ymin, ymax = -2, 2, -2, 2
npoints = 800
max_iter = 100
c = complex(0.285, 0.01)

x = torch.linspace(xmin, xmax, npoints)
y = torch.linspace(ymin, ymax, npoints)
X, Y = torch.meshgrid(x, y)
Z = X + 1j*Y

# 生成 Julia 集
julia = julia_set(Z, c, max_iter)

# 显示 Julia 集的图像
fig = plt.figure(dpi = 480)
fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
ax = plt.subplot()
plt.imshow(julia, cmap="hot")
plt.axis("off")
# plt.savefig(fname = "./Julia Set.png",dpi = 960)
plt.show()