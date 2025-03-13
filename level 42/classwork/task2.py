def find_maximum(arr):
    maxim = [0]

    for number in arr:
        if number > maxim:
            maxim = number


    return maxim

print(find_maximum([1, 2, 3, 4, 5]))

def num_multip_two(arr):
    result = 0

    for number in arr:
        if number > 0:
            result += number ** 2

    return result
print(num_multip_two([1, 2, 3, 4, 5]))