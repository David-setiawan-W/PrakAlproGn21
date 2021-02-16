'''
saya sedang berjalan - jalan di depan toko buku yang ternyata sedang mengadakan bazar, yang mana setiap bukunya dihargai Rp10.000 dan Rp25.000.
Pada saat itu juga saya mempunyai kupon potongan sebesar 25% untuk pembelian buku di toko tersebut, 
agar saya dapat menghitung jumlah buku yang saya akan beli dengan cepat beserta total
potongan yang saya dapat maka dibuatlah program penghitung dengan menerima input buku seharga Rp10.000 dan rp25.000 yang akan mengelompokkan total pembelian buku per harga lalu menghasilkan output per kelompok harga buku, 
harga sebelum kupon potongan, dan setelah potongan
'''

iniHarga10k = int(input('Masukan jumlah buku harga Rp10.000 :'))
iniHarga25k = int(input('Masukan jumlah buku harga Rp25.000 :'))

kelompokHargaBuku10k = 10000 * iniHarga10k
kelompokHargaBuku25k = 25000 * iniHarga25k

totalSebelumKupon = kelompokHargaBuku10k + kelompokHargaBuku25k

hargaSetelahKupon = totalSebelumKupon-(totalSebelumKupon*0.25)

print('Ini total harga buku yang Rp10.000 : ', kelompokHargaBuku10k)
print('Ini total harga buku yang Rp25.000 : ', kelompokHargaBuku25k)

print('Harga total sebelum kupon digunakan : ', totalSebelumKupon)
print('Harga buku setelah kupon : ', hargaSetelahKupon)