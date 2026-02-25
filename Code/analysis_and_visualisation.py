from helper import parse_file
from event_planner import brute_force, dynamic_programming_time_money
import random
import time
import matplotlib.pyplot as plt
import numpy as np

print("Enter file name with >= 28 different activities: ")
file = input()
total_activities, max_time, max_money, activities = parse_file(file)

n = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

y_brute = []
y_dp = []   
speed_up = []

for x in n:
    # create realistic additional test inputs
    sample = random.sample(activities, x)
    realistic_time = int(max_time * x/ total_activities)
    realistic_money = int(max_money * x/ total_activities)

    # brute Force
    start_time = time.perf_counter()
    a, b, c, d = brute_force(x, realistic_time, realistic_money, sample)
    end_time = time.perf_counter()
    print(f"at {x} brute force takes {end_time - start_time} seconds")
    y_brute.append(end_time - start_time)

    # dynamic Programming
    start_time = time.perf_counter()
    a, b, c, d = dynamic_programming_time_money(x, realistic_time, realistic_money, sample)
    end_time = time.perf_counter()
    print(f"at {x} dp takes {end_time - start_time} seconds")
    y_dp.append(end_time - start_time)

# calculate speed up
speed_up = np.array(y_brute) / np.array(y_dp)

# bf vs dp normal scale
plt.figure(figsize=(10,8))
plt.plot(n, y_brute, label="Brute Force", marker='o')
plt.plot(n, y_dp, label="Dynamic Programming", marker='s')
plt.xlabel("n (# of activities)")
plt.ylabel("Execution Time")
plt.title("Brute Force vs Dynamic Programming (normal scale)")
plt.legend()
plt.grid(True)
plt.show()

# bf vs dp log scale
plt.figure(figsize=(10,8))
plt.plot(n, y_brute, label="Brute Force", marker='o')
plt.plot(n, y_dp, label="Dynamic Programming", marker='s')
plt.yscale("log")
plt.xlabel("n (# of activities)")
plt.ylabel("Execution Time")
plt.title("Brute Force vs Dynamic Programming (log scale)")
plt.legend()
plt.grid(True)
plt.show()

# speed up plot
plt.figure()
plt.bar(n, speed_up)
plt.xlabel("n (# of activities)")
plt.ylabel("Speed-up Factor")
plt.title("brute time/ dp time")
plt.legend()
plt.show()
