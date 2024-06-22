
#Part 4


#Problem 1

def segitiga_asterik(tinggi):
    for i in range(1, tinggi + 1):
        # Mencetak spasi di awal baris
        print(' ' * (tinggi - i), end='')
        
        # Mencetak bintang sesuai dengan pola
        print('*' * (2 * i - 1))


segitiga_asterik(5)




#Problem 4

def geser_huruf(kalimat, pergeseran):
    hasil = ""
    for karakter in kalimat:
        # Periksa apakah karakter adalah huruf
        if karakter.isalpha():
            # Tentukan apakah huruf tersebut huruf besar atau kecil
            if karakter.islower():
                # Geser huruf ke depan, pergeseran modulus 26 untuk memastikan lingkaran alfabet
                baru = chr((ord(karakter) - ord('a') + pergeseran) % 26 + ord('a'))
            else:
                baru = chr((ord(karakter) - ord('A') + pergeseran) % 26 + ord('A'))
            hasil += baru
        else:
            # Jika bukan huruf, langsung tambahkan ke hasil
            hasil += karakter
    return hasil


kalimat = "SEPULSA OKE"
pergeseran = 10
hasil = geser_huruf(kalimat, pergeseran)
print("Kalimat setelah digeser:", hasil)



#Problem 5

import statistics

def hitung_mean(array):
    if len(array) == 0:
        return None
    return sum(array) / len(array)

def hitung_median(array):
    return statistics.median(array)


angka = [1,2,3,4,5]


mean = hitung_mean(angka)
print("Mean dari array:", mean)


median = hitung_median(angka)
print("Median dari array:", median)







