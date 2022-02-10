def flatten_nested_list(list: list):
    return [val for sublist in list for val in sublist]


def remove_duplicates_from_list(duplicate_list: list):
    return set(duplicate_list)
