
#Problem 1

def compare_string(a, b):
    # Menentukan string yang lebih pendek dan lebih panjang
    if len(a) > len(b):
        longer_str, shorter_str = a, b
    else:
        longer_str, shorter_str = b, a
    
    max_len = 0
    common_substr = ""

    # Mengurangi panjang substring dari lebih panjang sampai menemukan yang sama di yang lebih pendek
    for i in range(len(shorter_str)):
        for j in range(len(shorter_str) - i + 1):
            if j > max_len and shorter_str[i:i+j] in longer_str:
                max_len = j
                common_substr = shorter_str[i:i + j]
    return common_substr

# Contoh penggunaan:
a = "AKA"
b = "AKASHI"

hasil = compare_string(a, b)
print("Hasil compare string nya adalah:", hasil)




#Problem 2

def caesar(text, offset):
    encrypted_text = ""
    for char in text:
        # Periksa apakah karakter adalah huruf alfabet
        if char.isalpha():
            # Tentukan apakah karakter adalah huruf besar atau kecil
            start = ord('A') if char.isupper() else ord('a')
            # Enkripsi karakter dengan menggeser ASCII value
            encrypted_char = chr((ord(char) - start + offset) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Tambahkan karakter non-alfabet tanpa mengubahnya
            encrypted_text += char
    return encrypted_text


text = "abc"
offset = 3

# Enkripsi teks
encrypted_text = caesar(text, offset)
print("Encrypted:", encrypted_text)




#Problem 3

def array_unik(arr1, arr2):
    # Menggunakan set untuk menghapus duplikasi dan mendapatkan elemen unik dari arr2
    set_arr2 = set(arr2)
    
    # Membuat list yang berisi elemen dari arr1 yang tidak ada di set_arr2
    unique_array = [x for x in arr1 if x not in set_arr2]
    
    return unique_array

array1 = [1, 2, 3, 4]
array2 = [1, 3, 5, 10, 16]
result = array_unik(array1, array2)
print(result)



#Problem 4

def max_subarray_sum(angka, k):
    if k > len(angka):
        raise ValueError("Value dari 'k' tidak bisa lebih panjang daripada array.")
    
    max_sum = 0
    current_sum = sum(angka[:k])
    max_sum = current_sum
    
    for i in range(k, len(angka)):
        current_sum = current_sum + angka[i] - angka[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

angka = [2, 1, 5, 1, 3, 2]
k = 3
print("max subarray adalah:", max_subarray_sum(angka, k))




#Problem 5

def remove_duplikat(nums):
    if not nums:
        return 0
    
    next_non_duplikat = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[next_non_duplikat]:
            next_non_duplikat += 1
            nums[next_non_duplikat] = nums[i]
    
    return next_non_duplikat + 1


nums = [2, 3, 3, 3, 6, 9, 9]
length = remove_duplikat(nums)
print("berapa banyak angka setelah duplikat dihapus:", length)  
print("angka setelah duplikatnya dihapus:", nums[:length]) 




