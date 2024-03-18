def calculate_fuel_consumption_motor(distance, fuel_efficiency):
  """Menghitung konsumsi bahan bakar."""
  return distance / fuel_efficiency

def calculate_fuel_efficiency_motor(distance, fuel_consumption):
  """Menghitung efisiensi bahan bakar."""
  if fuel_consumption == 0:
    raise ValueError("Konsumsi bahan bakar tidak boleh 0.")
  return distance / fuel_consumption
