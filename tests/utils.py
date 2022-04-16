def lists_are_equal(list1: list, list2: list) -> bool:
    return len(list1) == len(list2) and all(el in list1 for el in list2)
