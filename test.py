#Вы должны установить matplotlib перед запуском говнокода

import matplotlib.pyplot as plt
import numpy as npy

g = 9.81
dt = 0.1
h0 = 19.6
y = 0 
v = 0 
t = 0
h = 1

t_arr = []
h_arr = []

t_arr.append(t)
h_arr.append(h0)


while h > 0:
    y += v*dt
    v += g*dt
    h = h0-y
    t+= dt
    print  (str(t) + "  " + "{:.3f}".format(y) + "  " + "{:.3f}".format(h) + "  " + "{:.3f}".format(v))
    t_arr.append (t)
    h_arr.append (h)


fix, ax = plt.subplots()
ax.plot(t_arr, h_arr)

ax.set (xlabel = 'время (с)', ylabel = 'высота (м)', title = 'график')

ax.grid()

plt.show()
