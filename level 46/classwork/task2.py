def no_duplicates(user_list):
    return list(set(user_list))
print(no_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(no_duplicates([True, False, False, True]))
print(no_duplicates(["a", "b", "c", "d", "e", "f", "g"]))