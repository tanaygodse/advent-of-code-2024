import matplotlib.pyplot as plt
import numpy as np
import time

with open("in") as f:
    lines = f.read().splitlines()

GRID_WIDTH = 101
GRID_HEIGHT = 103
TIME_DURATION = 10000

positions = []
velocities = []
for line in lines:
    p_part, v_part = line.split(" ")
    px, py = map(int, p_part.split("=")[1].split(","))
    vx, vy = map(int, v_part.split("=")[1].split(","))
    positions.append((px, py))
    velocities.append((vx, vy))

for t in range(TIME_DURATION + 1):
    positions = [
        ((px + vx) % GRID_WIDTH, (py + vy) % GRID_HEIGHT)
        for (px, py), (vx, vy) in zip(positions, velocities)
    ]
    x_arr = []
    y_arr = []
    for x, y in positions:
        x_arr.append(x)
        y_arr.append(y)
    xpoints = np.array(x_arr)
    ypoints = np.array(y_arr)
    if t > 6600:
        plt.figure()
        plt.plot(xpoints, ypoints, 'o')
        plt.xlim(0, GRID_WIDTH)
        plt.ylim(0, GRID_HEIGHT)
        plt.title(f"Time: {t} seconds")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
