import matplotlib.pyplot as plt
import torch

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
if __name__ == '__main__':
    xmin, xmax, ymin, ymax = -2, 2, -2, 2
    npoints = 800
    max_iter = 100
    c = complex(0.285, 0.01)
    
    x = torch.linspace(xmin, xmax, npoints)
    y = torch.linspace(ymin, ymax, npoints)
    X, Y = torch.meshgrid(x, y)
    Z = X + 1j*Y
    
    julia = julia_set(Z, c, max_iter)
    
    # Show julia set image
    fig = plt.figure(dpi = 480)
    fig.subplots_adjust(top=1, bottom=0, left=0, right=1)
    ax = plt.subplot()
    plt.imshow(julia, cmap="hot")
    plt.axis("off")
    # plt.savefig(fname = "./Julia Set.png",dpi = 960)
    plt.show()
