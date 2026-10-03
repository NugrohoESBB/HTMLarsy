# break and continue statement in python

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# angka = 1
# while angka <= 10:
#     if angka == 5:
#         break
#     print(angka)
#     angka += 1




# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# angka = 0
# while angka <= 10:
#     angka += 1
#     if angka == 5:
#         continue
#     print(angka)




# Seorang kasir ingin membuat program yang meminta pengguna memasukkan
# nominal uang hingga mencapai total minimal Rp50.000. Jika total yang
# dimasukkan kurang dari Rp50.000, maka program akan meminta pengguna untuk
# memasukkan uang lagi.

# Tugas:

# Buatlah program Python menggunakan while loop yang meminta pengguna untuk
# memasukkan nominal uang hingga total mencapai Rp50.000 atau lebih. Setelah
# itu, program menampilkan pesan:

totalUang = 0
while totalUang < 50000:
    tambahUang = int(input("Masukkan nominal uang: Rp"))
    totalUang += tambahUang
    print(f"total sementara: Rp{totalUang}")

print("")
print(f"total uang yg dimasukkan: Rp{totalUang}")

