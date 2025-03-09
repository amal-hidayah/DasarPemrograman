#Case 1

tahun = 2025
jenis = "ganjil"

if tahun % 4 == 0:
    jenis = "genap"
    
print("%s adalah tahun %s" % (tahun, jenis))

#Case 2

angka = int(input("Masukkan sebuah angka:"))

if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")
else:
    print("Nol")
    
#Case 3

nilai = int(input("Masukkan Total:"))
grade = "E"

if nilai >= 100:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
    
print("Grade:", grade)