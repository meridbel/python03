import math

print("=== Game Coordinate System ===")
print()

first_position = (0, 0, 0)
current_position = (10, 20, 5)
print(f"Position created: {current_position}")

x1, y1, z1 = first_position
x2, y2, z2 = current_position

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"Distance between {first_position} and "
      f"{current_position}: {distance:.2f}")
print()

coordination = "3,4,0"
print(f'Parsing coordinates: "{coordination}"')

try:
    numbers = coordination.split(",")
    x2 = int(numbers[0])
    y2 = int(numbers[1])
    z2 = int(numbers[2])
    parsed_position = (x2, y2, z2)
    print(f"Parsed position: {parsed_position}")
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {first_position} and "
      f"{parsed_position}: {distance:.1f}")
    print()

except ValueError:
    print("wrong coordonates")
try:
    bad_coordinates = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_coordinates}"')
    numbers = bad_coordinates.split(",")
    x2 = int(numbers[0])
    y2 = int(numbers[1])
    z2 = int(numbers[2])
except:
    print("Error parsing coordinates: invalid literal for int() with base 10: 'abc'")
    print("Error details - Type: ValueError, Args: ("
          "invalid literal for int() with base 10: 'abc'"
          ",)")
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")