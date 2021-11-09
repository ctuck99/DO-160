import math

# Enter in radius measurement (EUT center of gravity or nearest edge to centrifuge center)
r = float(input("Enter in radius (r) measurement in meters: "))

# Acceleration = 0.001118 * r * (RPM**2)

# Using 9g value for Fixed-Wing Transport per FAR 25.561...
# g / 0.00118 => 9 / 0.00118 = 8050.09 (rounded to nearest tenth)
# 8050.09 = R * (RPM**2)
# 8050.09 / R = (RPM**2) ---> R will be physically measured to find variable value

def calculate_RPM(r):
    result = math.sqrt(8050.09 / r)
    return result

rpm = calculate_RPM(r)

print(f"The RPM value per the radius given {r} is: {rpm}")

