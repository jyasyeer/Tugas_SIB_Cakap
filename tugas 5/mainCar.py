# Import modul yang dibutuhkan
from car.speed import *
from car.distance import *
from car.fuel import *
from pedestrian.pace import *
from pedestrian.distance import *
from pedestrian.calories import *
from motorcycle.speed import *
from motorcycle.distance import *
from motorcycle.fuel import *

# Menentukan jenis kendaraan
vehicle_type = input("Masukkan jenis kendaraan (mobil/pejalan kaki): ").lower()

if vehicle_type == "mobil":
  # Mendapatkan input data mobil
  distance_car = float(input("Masukkan jarak (km): "))
  time_car = float(input("Masukkan waktu (jam): "))
  fuel_efficiency_car = float(input("Masukkan efisiensi bahan bakar (km/l): "))

  # Menghitung kecepatan rata-rata mobil
  average_speed_car = calculate_average_speed_mobil(distance_car, time_car)

  # Menghitung total jarak yang ditempuh mobil
  distance_list_car = [distance_car]
  total_distance_car = calculate_total_distance_mobil(distance_list_car)


  # Menghitung konsumsi bahan bakar mobil
  fuel_consumption_car = calculate_fuel_consumption_mobil(distance_car, fuel_efficiency_car)

  # Menampilkan informasi mobil
  print(f"Kecepatan rata-rata mobil: {average_speed_car} km/jam")
  print(f"Total jarak yang ditempuh mobil: {total_distance_car} km")
  print(f"Konsumsi bahan bakar mobil: {fuel_consumption_car} l")

elif vehicle_type == "pejalan kaki":
  # Mendapatkan input data pejalan kaki
  distance_pedestrian = float(input("Masukkan jarak (km): "))
  time_pedestrian = float(input("Masukkan waktu (jam): "))
  weight_pedestrian = float(input("Masukkan berat badan (kg): "))

  # Menghitung waktu dalam menit
  time_pedestrian_minutes = time_pedestrian * 60

  # Menghitung kecepatan rata-rata pejalan kaki
  average_speed_pedestrian = calculate_average_speed_kaki(distance_pedestrian, time_pedestrian)

  # Menghitung total jarak yang ditempuh pejalan kaki
  distance_pedestrian_list = [distance_pedestrian]
  total_distance_pedestrian = calculate_total_distance_kaki(distance_pedestrian_list)

  # Menghitung pengeluaran energi pejalan kaki
  energy_expenditure_pedestrian = calculate_energy_expenditure_kaki(distance_pedestrian, weight_pedestrian, average_speed_pedestrian, time_pedestrian_minutes)

  # Menampilkan informasi pejalan kaki
  print(f"Kecepatan rata-rata pejalan kaki: {average_speed_pedestrian} km/jam")
  print(f"Total jarak yang ditempuh pejalan kaki: {total_distance_pedestrian} km")
  print(f"Pengeluaran energi pejalan kaki: {energy_expenditure_pedestrian} kalori")

elif vehicle_type == "motor": 
  # Mendapatkan input data motor
  distance_motor = float(input("Masukkan jarak (km): "))
  time_motor = float(input("Masukkan waktu (jam): "))
  fuel_efficiency_motor = float(input("Masukkan efisiensi bahan bakar (km/l): "))

  # Menghitung kecepatan rata-rata motor
  average_speed_motor = calculate_average_speed_motor(distance_motor, time_motor)

  # Menghitung total jarak yang ditempuh motor
  total_distance_motor = calculate_total_distance_motor(distance_motor)

  # Menghitung konsumsi bahan bakar motor
  fuel_consumption_motor = calculate_fuel_consumption_motor(distance_motor, fuel_efficiency_motor)

  # Menampilkan informasi motor
  print(f"Kecepatan rata-rata motor: {average_speed_motor} km/jam")
  print(f"Total jarak yang ditempuh motor: {total_distance_motor} km")
  print(f"Konsumsi bahan bakar motor: {fuel_consumption_motor} l")

else:
  print("Jenis kendaraan tidak valid. Masukkan 'mobil' atau 'pejalan kaki'.")
