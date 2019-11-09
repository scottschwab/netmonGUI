import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import requests
import time
from datetime import datetime

STEPS_IN_SECOND = 60
x = []
y = []
drops = 0

def animate(i):
    CUTOFF=100
    global drops, ax1
    with open("nettraffic2.log","a") as file:
        try:
            response = requests.head("https://google.com", timeout=2.50)
            lag = response.elapsed.total_seconds()
        except:
            lag = 0
            drops = drops + 1
        date = datetime.now()
        file.write(f"{date} | {lag}\n")
        file.flush()
        x.append(i)
        y.append(lag)
        misses = f"DROPS: {drops}"
    if len(x) > CUTOFF:
        x.pop(0)
        y.pop(0)
    ax1.clear()
    ax1.fill_between(x,0, y)
    ax1.text(x[0],0,misses)



#style.use('fivethirtyeight')
style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ani = animation.FuncAnimation(fig, animate, interval=STEPS_IN_SECONDS * 1000)
plt.show()


