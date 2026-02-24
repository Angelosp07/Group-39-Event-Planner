""" Module containing brute force and dynamic programming solutions to event planner problem """

from helper import parse_file

def brute_force(total_activities, max_time, max_money, activities):
    masks = generate_masks(total_activities)
    highest_enjoyment = 0
    best_activities = []

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

    return highest_enjoyment, best_activities

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

    for i in range(total_activities, 0, -1):
        if dp[i][t][m] != dp[i - 1][t][m]:
            activity = activities[i - 1]
            chosen_activities.append(activity)
            
            t -= activity[1]
            m -= activity[2]

    chosen_activities.reverse()
    return highest_enjoyment, chosen_activities


if __name__ == "__main__":
    file = input("Enter filename: ")

    total_activities, max_time, max_money, activities = parse_file(file)

    if activities is not None:
        best_enjoyment, chosen = dynamic_programming_time_money(
            total_activities, max_time, max_money, activities
        )

        print("\nBest enjoyment:", best_enjoyment)
        print("\nChosen activities:")

        for activity in chosen:
            print(activity)

        x, y = brute_force(total_activities, max_time, max_money, activities)
    
        print(f"Brute force result:\n{x}\n\n {y}")
