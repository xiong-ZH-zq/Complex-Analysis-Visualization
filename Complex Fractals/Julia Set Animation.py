import matplotlib.pyplot as plt
from matplotlib import animation
import torch    # use torch or cupy to accelerate
def julia_set(Z, c, max_iter):
    """Get julia set array
    :param Z: The surface complex set
    :param c: The constant
    :param max_iter: The max iteration number
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

def update_frame(num):
    julia = julia_set(Z, c-0.01j*num, max_iter)
    # update julia array
    image.set_array(julia)
    return image,

# Show and save the video. It will be long time to generate
ani = animation.FuncAnimation(fig, update_frame, frames=range(100), interval = 100, blit=True)
ani.save(filename='julia.mp4',writer='ffmpeg',fps = 24)
