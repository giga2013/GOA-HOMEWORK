numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# მხოლოდ ლუწი რიცხვების კვადრატში აყვანა
squares_of_even = [x**2 for x in numbers if x % 2 == 0]

print("ლუწი რიცხვების კვადრატები:", squares_of_even)
