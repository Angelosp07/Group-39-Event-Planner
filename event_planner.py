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

if __name__ == "__main__":
    total_activities, max_time, max_money, activities = parse_file(
        "input_files/input_medium.txt"
    )

    print(total_activities, max_time, max_money, activities)

    x, y = brute_force(total_activities, max_time, max_money, activities)

    print(f"\n{x}\n \n {y}")
