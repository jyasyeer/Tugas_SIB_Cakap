def calculate_distance_kaki(speed, time):
  """Menghitung jarak tempuh."""
  return speed * time

def calculate_total_distance_kaki(distance_list):
  """Menghitung total jarak yang ditempuh."""
  total_distance = 0
  for distance in distance_list:
    total_distance += distance
  return total_distance
