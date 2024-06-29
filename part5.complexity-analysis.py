

#Problem 1





#Problem 2

def pow (a, b):
    return a**b

print(pow (2,3))



#Problem 3

def join_array(array1, array2):
    
    # Menggabungkan kedua array
    join = array1 + array2
    
    # Menggunakan set untuk menghapus duplikat
    join_unik = list(set(join))
    
    return join_unik

array1 = ["Apel", "Nanas", "Anggur"]
array2 = ["Apel", "Pisang"]

hasil_join = join_array(array1, array2)
print("Hasil join array:")
print(hasil_join)



#Problem 4

def muncul_sekali(array):
   
    # Membuat dictionary untuk menghitung jumlah kemunculan setiap angka
    count = {}
    
    # Menghitung kemunculan setiap angka dalam array input
    for angka in array:
        if angka in count:
            count[angka] += 1
        else:
            count[angka] = 1
    
    # Membuat array untuk menyimpan angka yang hanya muncul satu kali
    hasil = []
    for key, value in count.items():
        if value == 1:
            hasil.append(key)
    
    return hasil

input_array = [1,2,3,4,3,2,1]
output_array = muncul_sekali(input_array)
print("Angka yang hanya muncul satu kali pada input:")
print(output_array)




#Problem 5

def pair_sum(arr, target):
    seen = set()  # Set untuk melacak nilai yang telah kita lihat sebelumnya
    pairs = []    # List untuk menyimpan pasangan-pasangan yang ditemukan
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    
    return pairs

arr = [1,2,3,4,6]
target = 6

hasil = pair_sum(arr, target)
print("Pair sum dari:", target, "adalah:", hasil)


