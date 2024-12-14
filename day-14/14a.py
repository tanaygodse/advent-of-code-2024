with open("in") as f:
    lines = f.read().splitlines()

GRID_WIDTH = 101
GRID_HEIGHT = 103
TIME_DURATION = 100

positions = []
velocities = []
for line in lines:
    p_part, v_part = line.split(" ")
    px, py = map(int, p_part.split("=")[1].split(","))
    vx, vy = map(int, v_part.split("=")[1].split(","))
    positions.append((px, py))
    velocities.append((vx, vy))

for t in range(TIME_DURATION):
    positions = [
        ((px + vx) % GRID_WIDTH, (py + vy) % GRID_HEIGHT)
        for (px, py), (vx, vy) in zip(positions, velocities)
    ]

mid_x = GRID_WIDTH // 2
mid_y = GRID_HEIGHT // 2

q1, q2, q3, q4 = 0, 0, 0, 0
for px, py in positions:
    if px == mid_x or py == mid_y:
        continue
    if px < mid_x and py < mid_y:
        q1 += 1
    elif px > mid_x and py < mid_y:
        q2 += 1
    elif px < mid_x and py > mid_y:
        q3 += 1
    elif px > mid_x and py > mid_y:
        q4 += 1

safety_factor = q1 * q2 * q3 * q4

print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}, Q4: {q4}")
print(safety_factor)
