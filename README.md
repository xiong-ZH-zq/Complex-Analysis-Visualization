# Complex-Analysis-Visualization
![Static Badge](https://img.shields.io/badge/Visualization-Python-blue)
![Static Badge](https://img.shields.io/badge/Animation-Manim-blue?link=https%3A%2F%2Fgithub.com%2FManimCommunity%2Fmanim)

----
基于多种编程语言的复分析可视化学习/Complex Analysis Visualization based on various programming languages
这是一个基于多种语言的复分析可视化学习，参考了特里斯坦尼达姆的《复分析：可视化方法》，由于一个学期的学习深度，有些复杂的内容不会出现。

同时本仓库也作为作者南开大学课程“Python科学计算”的课程大作业。
# 使用到的工具
虽然是作为Python科学计算的课程大作业，但是本仓库不局限于语言，追求以较好的可视化效果对《复分析：可视化方法》的案例进行可视化。同时也会涉及到复数生成的分形等内容，所以相对较为综合。

以下列出使用的工具以便配置。
## Python
- ![Manim Community](https://github.com/ManimCommunity/manim)
- ![Pytorch](https://github.com/pytorch/pytorch)
- ![Matplotlib](https://github.com/matplotlib/matplotlib)

## C语言
- ![Raylib](https://github.com/raysan5/raylib)



# 目录
## 基本内容
### 基本的复数概念与几何
- `ComplexPlane.py`
  复平面的建立与复数的可视化.
- `AComplexNumber.py`
复数的实部、虚部和模的展示.

### Euler公式
- `PowerSeriesEuler.py`
Euler公式的幂级数观点.

## 复变函数（解析函数）


## 复分形
本部分对计算的性能要求较高，尤其是动画的情况，利用 Python 等语言需要进行加速。
- 对于Python，可以考虑使用 `Pytorch` 进行加速，对整个二维矩阵进行向量化操作，使用`cupy`也能达到类似的效果.


### Julia集
- `Julia Set.py` Julia集的复数推导与绘图.
- `Julia.c` Julia集的C语言动画版本，使用 raylib 进行绘图.
