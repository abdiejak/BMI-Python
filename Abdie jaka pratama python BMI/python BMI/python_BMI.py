# PROGRAM BMI
# Mendapatkan berat badan user menggunakan tipe float untuk menerima bilangan bulat atau desimal
berat = float(input("Masukkan berat badan anda (kg) = "))
# Mendapatkan tinggi badan user menggunakan tipe float untuk menerima bilangan bulat atau desimal
tinggi = float(input("Masukkan tinggi badan anda (m) = "))
# Membuat rumus BMI = berat dibagi tinggi kuadrat
BMI = berat / tinggi**2

# Jika nilai BMI berada di antara 18.5 dan 22.9
if 18.5 <= BMI <= 22.9 :
    print("Normal")
# Jika nilai BMI berada lebih dari 22.9
elif BMI > 22.9 :
    print("OVERWEIGHT")
# Jika nilai BMI berada kurang dari 22.9
else :
    print("UNDERWEIGHT")