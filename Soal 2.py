#Soal 2
print('MENGHITUNG RATA-RATA NILAI')

n = int(input('Banyak nilai yang akan dimasukkan : '))
data = []
jumlah = 0

for i in range (0, n):
    nomor = int(input('Maukkan nilai ke-%d: ' %(i+1) ))
    data.append(nomor)
    jumlah += data[i]
    rerata = float (jumlah / n)

print('\nRata-rata = %0.2f' %rerata)
