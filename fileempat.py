# baca isi file dulu
nama_file = 'buah.txt'
handle = open(nama_file, 'r')
isi_file = handle.read()
print ("Isi file sekarang: ")
print (isi_file)
handle.close()

# setiap baris bertambah perlu enter atau tidak
perlu_enter = True
if isi_file[-1] == '\n':
    perlu_enter = False

# tambahkan satu baris di belakang
tambahan = input("Masukkan tambahan baris: ")
if perlu_enter:
    tambahan = '\n' + tambahan 

#simpan
handle = open(nama_file, 'a') #ra bertujuan untuk read dan append, rw bertujuan untuk read dan write
handle.write(tambahan)
handle.close()
