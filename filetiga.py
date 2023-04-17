nama_file = 'data.txt'
handle = open(nama_file, 'w') # write atau overwrite artunya tulisan yang lama ditimpa dengan tulisan yang baru

isi_file = input('Masukkan isi file: ')
handle.write(isi_file) # overwrite 
handle.close()

# jika belum ada file yang dituliskan di nama_file maka akan dibuat file baru tetapi jika sudah ada file yang ada maka isinya akan ditimpa dengan yang baru sehingga isi yang lama hilang


