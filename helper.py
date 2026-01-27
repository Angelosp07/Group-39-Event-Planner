""" Helper functions for data extraction etc """

def parse_file(file):
    """
    Parse inputted file.

    Args:
        file (str): filepath.

    Returns:
        int: total activities
        int: total time limit
        int: total money limit
        List[List[str, int, int, int]]: list of activities each containing their fields
    """
    activities = []
    try:
        with open(file, encoding='UTF-8') as f:
            #read first, second line and extract values
            total_activities = int(f.readline().strip())
            second_line = f.readline().split()
            max_time = int(second_line[0])
            max_money = int(second_line[1])

            for line in f:
                #read remaining lines to extract activities
                fields = line.rstrip().split()
                #ensuring correct types for each field
                activity = (fields[0],int(fields[1]), int(fields[2]), int(fields[3]))
                activities.append(activity)
        return total_activities, max_time, max_money, activities

    except FileNotFoundError:
        print("file not found")
        return None, None, None, None
