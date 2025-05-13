def flatten(lst):
    """
    Flattens a nested list.

    Args:
        lst (list): The list to flatten.

    Returns:
        list: A flattened version of the input list.
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
# Example usage
nested_list = [1, [2, 3], [[4], 5], 6]
flattened_list = flatten(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

def generator_flatten(lst):
    """
    A generator that yields elements from a nested list.

    Args:
        lst (list): The list to flatten.

    Yields:
        Elements from the flattened list.
    """
    for item in lst:
        if isinstance(item, list):
            yield from generator_flatten(item)
            """
            for sub_item in generator_flatten(item):
                yield sub_item
            """
        else:
            yield item
# Example usage
nested_list = [1, [2, 3], [[4], 5], 6]
flattened_gen = generator_flatten(nested_list)

def flatten_list(lst):
    """
    Flattens a nested list using a generator.

    Args:
        lst (list): The list to flatten.

    Returns:
        list: A flattened version of the input list.
    """
    return list(generator_flatten(lst))
# Example usage
nested_list = [1, [2, 3], [[4], 5], 6]
flattened_list = flatten_list(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]