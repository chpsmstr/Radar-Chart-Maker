def input_data(num_categories, num_observations, min_value, max_value):
    """
    Creates data for the radar chart.
    Number of categories must be greater than 2, so that the chart can be drawn.
    Minimum number of observations is 1.
    Minimum and maximum values are used to validate the input.
    """

    assert num_categories > 2
    assert num_observations > 0

    categories = []
    for i in range(num_categories):
        categories.append(input(f"Enter category {i+1}: "))

    data = dict()

    for i in range(num_observations):
        name = input(f"Enter name of observation {i+1}: ")
        values = []
        for j in range(num_categories):
            value = float(input(f"Enter value for {categories[j]}: "))
            if value < min_value or value > max_value:
                valid = False
                print(f"Value must be between {min_value} and {max_value}.\nTry again.")
                while not valid:
                    value = float(input(f"Enter value for {categories[j]}: "))
                    if value >= min_value and value <= max_value:
                        valid = True

            values.append(value)
        data[name] = values
    
    return categories, data