from coordinates import to_polar
from coordinates import to_cartesian_in_radian

vector_points = (-2, 3)

print("[Initial Cartesian] (x, y) = (" +
      str(vector_points[0])+", "+str(vector_points[1])+")")
polar_vector = to_polar(vector_points)

print("[Cartesian to Polar] (angle = "+str(polar_vector[0]) +
      ", vector length = "+str(polar_vector[1])+")")

cartesian_vector = to_cartesian_in_radian(polar_vector)

print("[Polar to Cartesian] (x, y) = (" +
      str(cartesian_vector[0])+", "+str(cartesian_vector[1])+")")
