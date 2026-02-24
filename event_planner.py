""" Module containing brute force and dynamic programming solutions to event planner problem """

from helper import parse_file
import time 

def brute_force(total_activities, max_time, max_money, activities):
    masks = generate_masks(total_activities)
    highest_enjoyment = 0
    best_activities = []
    best_time = 0
    best_cost = 0

    #for each mask
    for mask in masks:
        chosen_activities = []
        total_time = 0
        total_cost = 0
        total_enjoyment = 0
        #select masked activities
        for i, bit in enumerate(mask):
            if bit == "1":
                #append to chosen list, record totals of fields
                name, time, cost, enjoyment = activities[i]
                total_time += time
                total_cost += cost

                if total_time > max_time or total_cost > max_money:
                    break
                    
                total_enjoyment += enjoyment
                chosen_activities.append(activities[i])
        else:
            if total_enjoyment > highest_enjoyment:
                highest_enjoyment = total_enjoyment
                best_activities = chosen_activities
                best_time = total_time
                best_cost = total_cost

    return highest_enjoyment, best_time, best_cost, best_activities

def generate_masks(total_activities):
    num_masks = 2 ** total_activities
    masks = [
        bin(num)[2:].zfill(total_activities)
        for num in range(num_masks)
    ]
  
    return masks

def dynamic_programming_time(total_activities, max_time, max_money, activities):

    dp = [[0] * (max_time + 1) for _ in range(total_activities + 1)]

    # Build dp table
    for i in range(1, total_activities + 1):
        name, time_i, _, enjoy_i = activities[i - 1]

        for t in range(max_time + 1):

            if t >= time_i:
                dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - time_i] + enjoy_i)
            else:
                dp[i][t] = dp[i - 1][t]


    highest_enjoyment = dp[total_activities][max_time]

    # backtrack to find chosen activities
    chosen_activities = []
    t = max_time

    for i in range(total_activities, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            activity = activities[i - 1]
            chosen_activities.append(activity)
            t -= activity[1]

    chosen_activities.reverse()
    return highest_enjoyment, chosen_activities

def dynamic_programming_time_money(total_activities, max_time, max_money, activities):

    #3D dp table
    dp = [[[0] * (max_money + 1) for _ in range(max_time + 1)]
          for _ in range(total_activities + 1)]

    # Build dp table
    for i in range(1, total_activities + 1):
        name, time_i, cost_i, enjoy_i = activities[i - 1]

        for t in range(max_time + 1):
            for m in range(max_money + 1):
                
                if t >= time_i and m >= cost_i:
                    dp[i][t][m] = max(
                        dp[i - 1][t][m], 
                        dp[i - 1][t - time_i][m - cost_i] + enjoy_i
                    )
                else:
                    dp[i][t][m] = dp[i - 1][t][m]


    highest_enjoyment = dp[total_activities][max_time][max_money]

    # backtrack to find chosen activities
    chosen_activities = []
    t = max_time
    m = max_money
    best_time = 0
    best_cost = 0

    for i in range(total_activities, 0, -1):
        if dp[i][t][m] != dp[i - 1][t][m]:
            activity = activities[i - 1]
            chosen_activities.append(activity)

            best_time += activity[1]
            best_cost += activity[2]
            
            t -= activity[1]
            m -= activity[2]

    chosen_activities.reverse()
    return highest_enjoyment, best_time, best_cost, chosen_activities


if __name__ == "__main__":
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


        

