""" Module containing brute force and dynamic programming solutions to event planner problem """

from helper import parse_file

total_activities, max_time, max_money, activities = parse_file("input_files/input_medium.txt")

print(total_activities, max_time, max_money, activities)

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
                chosen_activities.append(activities[i])
                total_time += activities[i][1]
                total_cost += activities[i][2]
                total_enjoyment += activities[i][3]
        #check against constraints
        if total_time <= max_time and total_cost <= max_money:
            #check against current best combo
            if total_enjoyment > highest_enjoyment:
                #update best enjoyment, activities
                highest_enjoyment = total_enjoyment
                best_activities = chosen_activities

    return highest_enjoyment, best_activities

def generate_masks(total_activities):
    num_masks = 2 ** total_activities
    masks = []
    for num in range(num_masks):
        #convert denary to binary string, format, and add leading 0's
        mask = str(bin(num))[2:].zfill(total_activities)
        masks.append(mask)
    return masks




x, y = brute_force(total_activities, max_time, max_money, activities)

print(f"\n{x}\n \n {y}")
