#Soal 3
batas_bawah = 10
batas_atas = 25

for angka in range(batas_bawah, batas_atas):
   if angka % 2 == 0 or angka % 3 == 0 or angka % 5 == 0 or angka % 7 == 0:
       print('%d bukan prima' % angka)
       angka = angka + 1
   else:
       print('%d adalah bilangan prima' % angka)




