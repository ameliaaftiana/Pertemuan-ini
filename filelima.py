# baca isi file dulu
nama_file = 'buah.txt'
handle = open(nama_file, 'r')
isi_file = handle.read()
isi_file = isi_file.lower()

print ("Isi file sekarang: ")
print (isi_file)
handle.close()

# input user 
kata_lama = input ("Masukkan kata yang lama = ")
kata_lama = kata_lama.lower()


if isi_file.count(kata_lama) == 0:
    #tidak ada batal
    print (f'Kata {kata_lama} tidak ada di dalam file')
else:
    #kalau ada lakukan pergantian dengan metode replace
    kata_baru = input ("Masukkan kata yang baru = ")
    kata_baru = kata_baru.lower()
    handle = open(nama_file, 'w')
    isi_file = isi_file.replace(kata_lama, kata_baru)
    #tulis ke file
    handle.write(isi_file)
handle.close()
print (isi_file)

