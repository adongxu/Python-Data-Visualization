"""
填充两个轮廓线之间区域的例子
"""
from matplotlib.pyplot import figure, show, gca
import numpy as np

x = np.arange(0.0, 2, 0.01)

# two different signals are measured
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

fig = figure()
ax = gca()

# plot and fill between y1 and y2 where a logical condition is met
ax.fill_between(
    x,
    y1,
    y2,
    where=y2 >= y1,
    facecolors='darkblue',
    interpolate=True)
ax.fill_between(
    x,
    y1,
    y2,
    where=y2 <= y1,
    facecolors='deeppink',
    interpolate=True)

ax.set_title('filled between')

show()
