import matplotlib.pyplot as plt
from matplotlib import animation
import torch
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

julia = julia_set(Z, c, max_iter)
fig = plt.figure(dpi = 480)
image = plt.imshow(julia, cmap="hot")
plt.axis("off")
# plt.show()

# 定义更新帧的函数
def update_frame(num):
    julia = julia_set(Z, c-0.01j*num, max_iter)
    # 更新图像数据
    image.set_array(julia)
    # 返回一个包含更新的图形对象的元组
    return image,

# 创建动画对象
ani = animation.FuncAnimation(fig, update_frame, frames=range(100), interval = 100, blit=True)
ani.save(filename='julia.mp4',writer='ffmpeg',fps = 24)
