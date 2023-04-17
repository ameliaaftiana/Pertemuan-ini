keyword = input("Masukkan kata yang dicari = ")

# case insensitive = tidak peduli huruf besar/kecil
keyword = keyword.lower()

nama_file = 'brita.txt'
handle = open(nama_file, 'r') # read only mode text
jumlah = 0
# baca dengan for in
for baris in handle:
    baris = baris.lower()
    jumlah = jumlah + baris.count(keyword)
print(f'Ditemukan {jumlah} kata {keyword}')