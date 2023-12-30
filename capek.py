import math
import random

# Inisialisasi variabel
l, K, i, j, n, jml_datalatih, OUTPUT, kelasuji = 0, 0, 0, 0, 0, 0, 0, 0
zz, za, nilaig, nilaib, nilai1, nilai2, total, total1, kelas1, kelas2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
data = [[0] * 600 for _ in range(600)]
dataa = [[0] * 600 for _ in range(600)]
jarak = [0] * 600
nama = [0] * 1000
file = [0] * 1000
namafile = [0] * 1000

random.seed()
ulang = True

# Fungsi clrscr untuk membersihkan layar
def clrscr():
    print("\033c", end="")

clrscr()

print("\t     ====     KLASIFIKASI INDIAN LIVER PATIENT DENGAN ALGORITMA K-NN     ====")
print("\t     ====       UJIAN AKHIR SEMESTER MATA KULIAH KECERDASAN BUATAN       ==== ")
print("\t     ==================================================================")
print("\n")

# Baca data latih
knnILPD = open("data latih.txt", "r")
jml_datalatih = 500
n = jml_datalatih

for i in range(n):
    line = knnILPD.readline()
    values = line.strip().split('\t')  # Memisahkan baris menjadi nilai
    for j in range(9):
        data[i][j] = float(values[j])
knnILPD.close()

print("\n Penyimpanan output pada notepad : ")
file = input("\n   Nama file    : ")
OUTPUT = int(input("   Nomor urut file : "))

# Output notepad
file += f" ke-{OUTPUT}.txt"
namafile = file
KNN = open(namafile, "w")
KNN.write("\t     ====     KLASIFIKASI INDIAN LIVER PATIENT DENGAN ALGORITMA K-NN     ====\n")
KNN.write("\t     ====       UJIAN AKHIR SEMESTER MATA KULIAH KECERDASAN BUATAN       ==== \n")
KNN.write("\t     ==================================================================\n\n")

# Input Data Uji
K = int(input("Masukkan jumlah tetangga terdekat (K) : "))
print("\n DATA UJI \n")
TB = float(input("Masukkan nilai Total Bilirubin (TB) : "))
DB = float(input("Masukkan nilai Direct Bilirubin (DB) : "))
ALP = float(input("Masukkan nilai Alkaline Phosphotase (ALP) : "))
SGPT = float(input("Masukkan nilai Serum Glutamic Pyruvic Transaminase (SGPT) : "))
SGOT = float(input("Masukkan nilai Serum Glutamat Oksaloasetat Transaminase (SGOT) : "))
TP = float(input("Masukkan nilai Total Protein (TP) : "))
ALB = float(input("Masukkan nilai Albumin (ALB) : "))
AG = float(input("Masukkan nilai Albumin Globulin (A/G) : "))
KNN.write("\n======================================================================================================================\n")
print("\n Output secara lengkap dapat dilihat pada file => ", namafile)
KNN.write("\n Output secara lengkap dapat dilihat pada file => " + namafile + "\n")

# PENGABUNGAN DATA LATIH DAN UJI
KNN.write("\n DATA LATIH DAN DATA UJI \n")
KNN.write("TB\t DB\t ALP\t SGPT\t SGOT\t TP\t ALB\t AG\t CLASS\n")

# Pada loop berikut, Anda mengganti range menjadi 500 dan mengakses data[i], tetapi mungkin dimaksudkan untuk menggunakan data[500]
for i in range(501):
    data[500][0] = TB
    data[500][1] = DB
    data[500][2] = ALP
    data[500][3] = SGPT
    data[500][4] = SGOT
    data[500][5] = TP
    data[500][6] = ALB
    data[500][7] = AG
    data[500][8] = 0

    # Perbarui range ke 9 agar mencakup semua kolom
    for j in range(9):
        KNN.write(f"{data[500][j]:.3f}\t ")
    KNN.write("\n")

# NORMALISASI
# Nilai MAX DAN MIN
KNN.write("\n NILAI MAXIMUM DAN MINIMUM TIAP KOLOM \n")
max_values = [0] * 8
min_values = [100000] * 8

KNN.write("\t MAXIMUM\t MINIMUM\n")

for i in range(n + 1):
    for j in range(8):
        if min_values[j] > data[i][j]:
            min_values[j] = data[i][j]
        if max_values[j] < data[i][j]:
            max_values[j] = data[i][j]

for i in range(8):
    KNN.write(f"{['TB', 'DB', 'ALP', 'SGPT', 'SGOT', 'TP', 'ALB', 'AG'][i]} : \t {max_values[i]} \t \t {min_values[i]}\n")

KNN.write("\n======================================================================================================================\n")

# TABEL NORMAL
KNN.write("\n TABEL SETELAH DINORMALISASI \n")
KNN.write("NO\t\t TB\t\t DB\t\t ALP\t\t SGPT\t\t SGOT\t\t TP\t\t ALB\t\t AG\t\t CLASS\n")

for j in range(n + 1):
    dataa[j][0] = ((data[j][0] - min_values[0]) / (max_values[0] - min_values[0]))
    dataa[j][1] = ((data[j][1] - min_values[1]) / (max_values[1] - min_values[1]))
    dataa[j][2] = ((data[j][2] - min_values[2]) / (max_values[2] - min_values[2]))
    dataa[j][3] = ((data[j][3] - min_values[3]) / (max_values[3] - min_values[3]))
    dataa[j][4] = ((data[j][4] - min_values[4]) / (max_values[4] - min_values[4]))
    dataa[j][5] = ((data[j][5] - min_values[5]) / (max_values[5] - min_values[5]))
    dataa[j][6] = ((data[j][6] - min_values[6]) / (max_values[6] - min_values[6]))
    dataa[j][7] = ((data[j][7] - min_values[7]) / (max_values[7] - min_values[7]))

    KNN.write(f"{j+1}\t\t {dataa[j][0]:.1f}\t\t {dataa[j][1]:.1f}\t\t {dataa[j][2]:.1f}\t\t {dataa[j][3]:.1f}\t\t {dataa[j][4]:.1f}\t\t {dataa[j][5]:.1f}\t\t {dataa[j][6]:.1f}\t\t {dataa[j][7]:.1f}\t\t {data[j][8]:.1f}\n")

# MENGHITUNG JARAK
KNN.write("\n======================================================================================================================\n")
KNN.write("\n TABEL JARAK EUCLID \n")
KNN.write("NO\t JARAK\t CLASS\n")

# hitung jarak
for j in range(n):
    jarak[j] = math.sqrt(
        sum((dataa[j][k] - dataa[n][k]) ** 2 for k in range(8))
    )
    KNN.write(f"{j + 1}\t {jarak[j]:.2f}\t {data[j][8]}\n")

KNN.write("\n\n")
KNN.write("\n======================================================================================================================\n")

# PENGURUTAN
for l in range(n):
    for j in range(n - 1):
        if jarak[j] > jarak[j + 1]:
            jarak[j], jarak[j + 1] = jarak[j + 1], jarak[j]
            data[j][8], data[j + 1][8] = data[j + 1][8], data[j][8]

KNN.write("  JARAK TERDEKAT DENGAN JARAK UJI\n")
KNN.write("NO.\t Jarak\t Class\n")

for l in range(K):
    KNN.write(f"{l + 1}\t {jarak[l]:.2f}\t {data[l][8]}\n")

nilaig = 0
nilaib = 0
total1 = 0

# menghitung membership function tiap kelas
for l in range(K):
    if data[l][8] == 1:
        nilai1 = pow(jarak[l], (-2))
        nilaig += nilai1
    elif data[l][8] == 2:
        nilai2 = pow(jarak[l], (-2))
        nilaib += nilai2
    total = pow(jarak[l], (-2))
    total1 += total

kelas1 = nilaig / total1
kelas2 = nilaib / total1

# menentukan kelas klasifikasi data uji
if kelas1 > kelas2:
    kelasuji = 1
else:
    kelasuji = 2

KNN.write("\n")
KNN.write("\n======================================================================================================================\n")
KNN.write("\t\t KLASIFIKASI DATA UJI \n")
KNN.write("TB\t DB\t ALP\t SGPT\t SGOT\t TP\t ALB\t AG\t CLASS\n")
KNN.write(f"{TB:.3f}\t {DB:.3f}\t {ALP:.3f}\t {SGPT:.3f}\t {SGOT:.3f}\t {TP:.3f}\t {ALB:.3f}\t {AG:.3f}\t {kelasuji:.3f}")

if kelasuji == 1:
    KNN.write("\n\t\t Anda Didiagnosa Liver Disorder")
else:
    KNN.write("\n\t\t Selamat, Anda baik-baik saja")

KNN.write("\n")

