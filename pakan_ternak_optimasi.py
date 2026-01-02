from pulp import *

# Membuat masalah optimasi
masalah = LpProblem("Optimasi_Pakan_Ternak", LpMinimize)

# Variabel keputusan
pakan_A = LpVariable("Pakan_A_kg", 0, None)  # Jumlah pakan A dalam kg
pakan_B = LpVariable("Pakan_B_kg", 0, None)  # Jumlah pakan B dalam kg

# Fungsi tujuan: Minimalisasi biaya
masalah += 10000 * pakan_A + 8000 * pakan_B, "Total_Biaya"

# Kendala
# Kebutuhan protein minimal 18 unit: 3A + 2B ≥ 18
masalah += 3*pakan_A + 2*pakan_B >= 18, "Kebutuhan_Protein"

# Kebutuhan energi minimal 24 unit: 2A + 4B ≥ 24
masalah += 2*pakan_A + 4*pakan_B >= 24, "Kebutuhan_Energi"

# Menyelesaikan masalah
masalah.solve()

# Menampilkan hasil
print("\n=== HASIL OPTIMASI PAKAN TERNAK ===")
print(f"Status: {LpStatus[masalah.status]}")
print(f"\nJumlah Pakan A yang dibutuhkan: {pakan_A.varValue:.2f} kg")
print(f"Jumlah Pakan B yang dibutuhkan: {pakan_B.varValue:.2f} kg")
print(f"\nTotal biaya minimum: Rp {value(masalah.objective):,.2f}")

# Verifikasi
print("\n=== VERIFIKASI KEBUTUHAN ===")
print(f"Total Protein: {3*pakan_A.varValue + 2*pakan_B.varValue:.1f} unit (minimal 18)")
print(f"Total Energi: {2*pakan_A.varValue + 4*pakan_B.varValue:.1f} unit (minimal 24)")

# Informasi tambahan
print("\n=== INFORMASI BAHAN PAKAN ===")
print("Harga Pakan A: Rp 10.000 per kg")
print("Harga Pakan B: Rp 8.000 per kg")
print("\nKandungan per kg:")
print("- Pakan A: 3 unit protein, 2 unit energi")
print("- Pakan B: 2 unit protein, 4 unit energi")