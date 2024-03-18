def calculate_fuel_consumption_mobil(distance, fuel_efficiency):
  """Menghitung konsumsi bahan bakar."""
  return distance / fuel_efficiency

def calculate_fuel_efficiency_mobil(distance, fuel_consumption):
  """Menghitung efisiensi bahan bakar."""
  if fuel_consumption == 0:
    raise ValueError("Konsumsi bahan bakar tidak boleh 0.")
  return distance / fuel_consumption

def calculate_carbon_emission_mobil(fuel_consumption, emission_factor):
  """Menghitung emisi gas buang."""
  return fuel_consumption * emission_factor
