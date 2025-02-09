def find_minimum(user_list):
    minimum= user_list[0]

    for num in user_list:
        if num < minimum:
            minimum = num

    print(minimum)

find_minimum ([4, 5, 6, 7, 8])
find_minimum ([5, 6, 7, 8, 9])
find_minimum ([6, 7, 8, 9, 10])
find_minimum ([7, 8, 9, 10, 11])
find_minimum ([8, 9, 10, 11, 12])