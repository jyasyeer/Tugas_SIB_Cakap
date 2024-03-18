def calculate_average_speed_kaki(distance, time):
  """Menghitung kecepatan rata-rata."""
  if time == 0:
    raise ValueError("Waktu tidak boleh 0.")
  return distance / time

def calculate_instantaneous_speed_kaki(distance_list, time_list):
  """Menghitung kecepatan sesaat pada setiap interval waktu."""
  if len(distance_list) != len(time_list):
    raise ValueError("Panjang daftar jarak dan waktu harus sama.")
  instantaneous_speed_list = []
  for distance, time in zip(distance_list, time_list):
    if time == 0:
      raise ValueError("Waktu tidak boleh 0.")
    instantaneous_speed_list.append(distance / time)
  return instantaneous_speed_list
