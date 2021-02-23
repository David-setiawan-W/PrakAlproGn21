'''
saya sedang berjalan - jalan di depan toko buku yang ternyata sedang mengadakan bazar, yang mana setiap bukunya dihargai Rp10.000 dan Rp25.000.
Pada saat itu juga saya mempunyai kupon potongan sebesar 25% yang dapat digunakan untuk pembelian buku di toko tersebut jika total pembelian minimal Rp150.000,
juga kupon potongan untuk buku seharga Rp10.000 sebesar 10% yang akan saya dapat jika membeli 4 buku atau lebih, 20% jika lebih dari 8 buku
agar saya dapat menghitung jumlah buku yang saya akan beli dengan cepat beserta total
potongan yang saya dapat dan juga memsatikan saya tidak kekurangan uang untuk membeli buku" tersebut.
maka dibuatlah program penghitung dengan menerima input uang yang saya bawa kemudian buku seharga Rp10.000 dan rp25.000 yang akan mengelompokkan total pembelian buku per harga 
lalu menghasilkan output per kelompok harga buku beserta potongan yang didapat, harga sebelum kupon potongan, dan setelah potongan, konfirmasi bahwa uang yang saya bawa mencukupi atau tidak.
'''

UangYangSayaBawa = int(input('Masukan Jumlah Uang Yang Saya Bawa : '))
iniHarga10k = int(input('Masukan jumlah buku harga Rp10.000 :'))
iniHarga25k = int(input('Masukan jumlah buku harga Rp25.000 :'))

if iniHarga10k >= 4 and iniHarga10k <=8:
    kelompokHargaBuku10k = (10000 * iniHarga10k) - ((10000 * iniHarga10k)*0.1)
elif iniHarga10k > 8:
    kelompokHargaBuku10k = (10000 * iniHarga10k) - ((10000 * iniHarga10k)*0.2)
else :
    kelompokHargaBuku10k = 10000 * iniHarga10k

kelompokHargaBuku25k = 25000 * iniHarga25k

totalSebelumKupon = kelompokHargaBuku10k + kelompokHargaBuku25k

print('Ini total harga buku yang Rp10.000 : ', kelompokHargaBuku10k)
print('Ini total harga buku yang Rp25.000 : ', kelompokHargaBuku25k)

print('Harga total sebelum kupon digunakan : ', totalSebelumKupon)

if totalSebelumKupon >= 150000:
    hargaSetelahKupon = totalSebelumKupon-(totalSebelumKupon*0.25)
    konfirmasi = UangYangSayaBawa - hargaSetelahKupon
    if konfirmasi >= 0:
        print('\nSaya Dapat Membeli Buku Tersebut')
        print('Harga buku Yang Harus Dibayar : ', hargaSetelahKupon)
    else :
        print('\nUang Yang Saya Bawa Kurang Dari Total Pembayaran')
else :
    konfirmasi = UangYangSayaBawa - totalSebelumKupon
    if konfirmasi >= 0:
        print('\nSaya Dapat Membeli Buku Tersebut')
        print('\nTotal Harga Buku Yang Harus dibayar : ', totalSebelumKupon)
    else :
        print('\nUang Yang Saya Bawa Kurang Dari Total Pembayaran')
    