print("PROGRAM MENENTUKAN NILAI INDEKS MAHASISWA")
nama = str(input("\nMasukkan Nama: "))
npm = int(input("Masukkan NPM: "))
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

n_akhir =  (0.15 * uas) + (0.35 * uts) +  (0.50 * uas)
if n_akhir >= 80:
    indeks = 'A'
elif n_akhir >= 70:
    indeks = 'B'
elif n_akhir >= 55:
    indeks = 'C'
elif n_akhir >= 40:
    indeks = 'D'
else:
    indeks = 'E'

print("\nNama       = %s" % nama)
print("NPM          = %i" % npm)
print("Nilai Akhir  = %0.2f" % n_akhir)
print("Nilai Indeks = %c" % indeks)
