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
            max_time, max_money = map(int, f.readline().split())

            for line in f:
                #read remaining lines to extract activities
                name, time, cost, enjoyment = line.strip().split()
                #ensuring correct types for each field, use of tuple (immutable)
                activities.append((name, int(time), int(cost), int(enjoyment)))
                
        return total_activities, max_time, max_money, activities

    except (FileNotFoundError, ValueError) as e:
        print(f"error: {e}")
        return None, None, None, None
