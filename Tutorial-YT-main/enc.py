# modul
import os,sys,time
import marshal


# input
file = input("nama File : ")

# baca isi file
baca = open(file,'r').read()

# compile file yg sudah di baca
com = compile(baca, "","exec")

# encypt file yg sudah di compile menggunakan marshal
encypt = marshal.dumps(com)

# membuat file baru
baru = open("enc_"+str(file), 'w')


# print kode marshal
baru.write("import marshal\n")
baru.write("exec(marshal.loads("+repr(encypt)+"))")

# hasil
print("Berhasil di enc | file enc_"+str(file))


# Simpan CTRL X Y
