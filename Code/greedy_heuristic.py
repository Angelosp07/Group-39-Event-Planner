from helper import parse_file
from event_planner import brute_force, dynamic_programming_time_money
import time 

def greedy_heuristic(total_activities, max_time, max_money, activities):
    activities_ratio = []
    # calculate enjoyment per hour ratio for each activity and store in array
    for i in range(total_activities):
        name, time, cost, enjoyment = activities[i]
        enjoyment_per_hour = enjoyment / time
        activities_ratio.append([name, time, cost, enjoyment, enjoyment_per_hour])
    # sort by ratio biggest to smallest
    activities_ratio_sorted = sorted(activities_ratio, key=lambda x: x[4], reverse=True)

    highest_enjoyment = 0
    best_activities = []
    best_time = 0
    best_cost = 0

    # iterate through list and append if fitting time and money constraints
    for i in range(total_activities):
        name, time, cost, enjoyment, ratio = activities_ratio_sorted[i]

        if best_time + time <= max_time:
            if best_cost + cost <= max_money:
                best_activities.append([name, time, cost, enjoyment])
                best_time += time
                best_cost += cost
                highest_enjoyment += enjoyment

    return highest_enjoyment, best_time, best_cost, best_activities

# compare algorithms
activities = None
    
while activities is None:
    file = input("Enter filename: ")
    total_activities, max_time, max_money, activities = parse_file(file)

    if activities is None:
        print("No activities found in file, try again")

print()
print("File parsed successfully.")
print()
print("========================================")
print("EVENT PLANNER - RESULTS")
print("========================================")
print()

print(f"Input File: {file.split('/')[-1]}")
print(f"Available Time: {max_time} hours")
print(f"Available Budget: £{max_money}")
print()

print("--- GREEDY HEURISTIC ALGORITHM ---")

start_time = time.perf_counter()
highest_enjoyment, best_time, best_cost, best_activities = greedy_heuristic(total_activities, max_time, max_money, activities)
end_time = time.perf_counter()

print("Selected Activities:")
for activity in best_activities:
    print(f" - {activity[0]} ({activity[1]} hours, £{activity[2]}, enjoyment: {activity[3]})")
print()

print(f"Total Enjoyment: {highest_enjoyment}")
print(f"Total Time Used: {best_time} hours")
print(f"Total Cost: £{best_cost}")
print()

print(f"Execution Time: {end_time - start_time:.3f} seconds")
print()

print("--- BRUTE FORCE ALGORITHM ---")

start_time = time.perf_counter()
highest_enjoyment, best_time, best_cost, best_activities = brute_force(total_activities, max_time, max_money, activities)
end_time = time.perf_counter()

print("Selected Activities:")
for activity in best_activities:
    print(f" - {activity[0]} ({activity[1]} hours, £{activity[2]}, enjoyment: {activity[3]})")
print()

print(f"Total Enjoyment: {highest_enjoyment}")
print(f"Total Time Used: {best_time} hours")
print(f"Total Cost: £{best_cost}")
print()

print(f"Execution Time: {end_time - start_time:.3f} seconds")
print()

print("--- DYNAMIC PROGRAMMING ALGORITHM ---")
start_time = time.perf_counter()
highest_enjoyment, best_time, best_cost, best_activities = dynamic_programming_time_money(total_activities, max_time, max_money, activities)
end_time = time.perf_counter()

print("Selected Activities:")
for activity in best_activities:
    print(f" - {activity[0]} ({activity[1]} hours, £{activity[2]}, enjoyment: {activity[3]})")
print()

print(f"Total Enjoyment: {highest_enjoyment}")
print(f"Total Time Used: {best_time} hours")
print(f"Total Cost: £{best_cost}")
print()

print(f"Execution Time: {end_time - start_time:.3f} seconds")
print()
    
print("========================================")
