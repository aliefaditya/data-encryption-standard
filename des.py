"""
    This program owned by Alief

    Req : 
    - Untuk Messagenya pake 8 karakter dari nama terus diubah ke biner sesuai ascii.
    - Untuk Keynya pake 10 digit nim + 6 digit terakhir nim. Semuanya digitnya diubah ke biner dengan panjang 4 bit 
"""

#Message 
charAscii = []
nama = ['a','l','i','e','f','a','d','i']
#konversi ke ascii
for i in range(8):
    charAscii[i] = ord(nama[i])
print(charAscii)
#konversi ke biner untuk setiap ascii

#key 10 digit nim + 6 digit nim
key = [1,3,0,1,1,7,4,0,5,5,1,7,4,0,5,5]
#konversi ke biner dengan panjang 4 bit

