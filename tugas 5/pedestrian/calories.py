def calculate_energy_expenditure_kaki(distance, weight, speed, time_in_minutes):
    """Menghitung pengeluaran energi."""
    # Rumus MET (Metabolic Equivalent of Task) untuk berjalan
    met = 0.75 + (0.057 * speed) + (0.00098 * weight)
    # Konversi MET ke kalori per menit
    calories_per_minute = met * 3.5 * weight / 200
    # Menghitung total kalori yang terbakar
    total_calories = calories_per_minute * time_in_minutes
    return total_calories
