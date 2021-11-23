x = int(input("Masukkan x: "))
for i in range(x):
    arr[i] = int(input("Kondisi titik ke-" + str(i) + ": "))

c = int(input("Masukkan titik lokasi bom [C]: "))
arr[c] = 0
l = int(input("Masukkan daya ledak bom [L]: "))
for i in range(c - l, c + l):
    arr[i] = 0
count = 0
for i in range(x):
    if arr[i] == 1:
        count += 1

print("Ada", count, "tempat yang bisa kamu tempati")