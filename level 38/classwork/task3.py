def rectangle_info(side1, side2):
    return (side1 + side2) * 2, side1 * side2

perimeter, area = rectangle_info(10, 5)
print(perimeter)
print(area)