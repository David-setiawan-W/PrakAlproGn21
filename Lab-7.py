#saya ingin membuat sebuah program untuk mengubah kalimat menjadi kode ascii kemudian dikonversi kedalam bilangan hexadesimal untuk menjaga kerahasiaan kalimat yang saya tuliskan
iniMasukan = input('Masukan Kalimat yang ingin dikonversi : ')
for i in iniMasukan:
    konversi = ord(i)
    print(format(konversi,'X'),end='')