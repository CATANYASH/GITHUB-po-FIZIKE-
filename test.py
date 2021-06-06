#Вы должны установить matplotlib перед запуском говнокода
#xlsxwriter - пакет для работы с Excel-файлами

import matplotlib.pyplot as plt
import xlsxwriter

g = 9.81
dt = 0.1
h0 = 19.6
y = 0 
v = 0 
t = 0
h = 1

i = 1

t_arr = []
h_arr = []

t_arr.append(t)
h_arr.append(h0)

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('test2.xlsx')
worksheet = workbook.add_worksheet()

#Заголовок таблицы
worksheet.write_row(0, 0, ['t', 'y', 'h', 'v'])




while h > 0:
    y += v*dt
    v += g*dt
    h = h0-y
    t+= dt
    print  (str(t) + "  " + "{:.3f}".format(y) + "  " + "{:.3f}".format(h) + "  " + "{:.3f}".format(v))
    t_arr.append (t)
    h_arr.append (h)
    worksheet.write_row(i, 0, ["{:.1f}".format(t), "{:.3f}".format(y), "{:.3f}".format(h), "{:.3f}".format(v)])
    i+=1


fix, ax = plt.subplots()
ax.plot(t_arr, h_arr, 'r-')

ax.set (xlabel = 'время (с)', ylabel = 'высота (м)', title = 'график')

ax.grid()

workbook.close()
plt.show()
ax.grid()

plt.show()
