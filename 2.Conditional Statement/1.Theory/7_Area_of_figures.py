from math import pi
shape = input()
area = float()

if shape == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

elif shape == "circle":
    radius = float(input())
    area = pi * radius ** 2
    print(f"{area:.3f}")

elif shape == "triangle":
    side_a = float(input())
    high = float(input())
    area = (side_a * high) / 2
    print(f"{area:.3f}")
