def calculate_distance_mobil(speed, time):
  """Menghitung jarak tempuh."""
  return speed * time

def calculate_distance_with_acceleration_mobil(initial_speed, acceleration, time):
  """Menghitung jarak tempuh dengan percepatan."""
  return initial_speed * time + 0.5 * acceleration * time**2

def calculate_total_distance_mobil(distance_list):
  """Menghitung total jarak yang ditempuh."""
  total_distance = 0
  for distance in distance_list:
    total_distance += distance
  return total_distance
