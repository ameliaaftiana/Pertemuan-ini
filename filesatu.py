nama_file = 'D:\\71220867\\data.txt'
# windows
# nama_file = 'D:\\Android\\data.txt'

#linux
# nama_file = 'var/www/data.txt'

handle = open(nama_file, 'r') # read only mode teks, (rb) read only mode binary
# mode = r, w, a, b -> binary

n = 2
no_baris = 1
for baris in handle: #digunakan untuk membaca per bari
    if no_baris == n :
        # hanya menampilkan baris ke-n saja
        print(baris, end='')
    no_baris = no_baris + 1
    
# harus selalu dilakukan
handle.close()

# cara membaca isi file ada 3 cara:
# (hasil = handle.read()) #digunakan untuk membaca keseluruhan file/string
# (hasil = handle.readline()) #digunakan untuk membaca baris saat itu/string, 1 baris di posisi sekarang
# (hasil = handle.readlines()) #digunakan untuk membaca semua baris tapi dimasukkan ke dalam list/list berisi semua baris

hasil = handle.readlines()
print(hasil)
print(f'Ada {len(hasil)} baris')
