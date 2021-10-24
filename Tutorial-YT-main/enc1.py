#modul
import marshal, zlib, base64, os, sys

try:
   r = sys.argv[1]
except:
   exit("usage : python2 enc1.py file.py")

if not os.path.isfile(r): #yang r sama in kaya di atas
   exit("File tidak di temukan")

a = open(r).read()
b = marshal.dumps(a) #yang a sama kaya di atas b
c = zlib.compress(b) #yang b sama kaya di atas c
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open("hasil.py","w").write(sv.format(d))
exit("berhasil : save to as hasil.py")

#simpan ctrl x y
