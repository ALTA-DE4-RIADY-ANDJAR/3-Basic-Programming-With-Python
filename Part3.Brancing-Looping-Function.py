
#Problem 1

def konversi_nilai(score):
    if score >= 80:
        return 'A'
    elif 65 <= score <= 79:
        return 'B+'
    elif 50 <= score <= 64:
        return 'B'
    elif 35 <= score <= 49:
        return 'C'
    elif 0 <= score <= 34:
        return 'D'
    else:
        return 'E'
    
nilai = 64
grade = konversi_nilai(nilai)
print (grade)



#Problem 2.1

def mencari_factors(angka):
    factors = []
    # Loop dari 1 sampai angka
    for i in range(1, angka + 1):
        if angka % i == 0:
            factors.append(i)
    return factors

bilangan = 20
faktor_bilangan = mencari_factors(bilangan)
print(f"Faktor dari bilangan {bilangan} adalah:", faktor_bilangan)


#Problem 2.2

def mencari_factors_tersusun(angka):
    factors = []
    # Loop dari 1 sampai angka
    for i in range(1, angka + 1):
        if angka % i == 0:
            factors.append(i)

    factors_tersusun = sorted (factors, reverse=True)
    return factors_tersusun

bilangan = 20
faktor_bilangan = mencari_factors_tersusun(bilangan)
print(f"Faktor dari bilangan {bilangan} adalah:", faktor_bilangan)



#Problem 3

def isprime(angka):
    # Bilangan prima harus lebih besar dari 1
    if angka <= 1:
        return False
    
    # 2 dan 3 adalah bilangan prima khusus
    if angka <= 3:
        return True
    
    # Bilangan genap selain 2 bukan bilangan prima
    if angka % 2 == 0:
        return False
    
    # Cek faktor dari 3 hingga akar dari angka
    i = 3
    while i * i <= angka:
        if angka % i == 0:
            return False
        i += 2
    
    return True

bilangan = 17 
if isprime(bilangan):
    print(f"{bilangan} adalah bilangan prima")
else:
    print(f"{bilangan} bukan bilangan prima")



#Problem 4

def ispalindrome(kata):
    # Menghilangkan spasi dan mengubah ke huruf kecil
    kata = kata.replace(" ", "").lower()
    
    # Memeriksa apakah kata sama jika dibalik
    return kata == kata[::-1]


kata = "level"
if ispalindrome(kata):
    print(f"{kata} adalah palindrome.")
else:
    print(f"{kata} bukan palindrome.")

kata = "buku"
if ispalindrome(kata):
    print(f"{kata} adalah palindrome.")
else:
    print(f"{kata} bukan palindrome.")



#Problem 5

def perpangkatan(base, pangkat):
    result = base ** pangkat
    return result

base = 2
pangkat = 3
hasil = perpangkatan(base, pangkat)
print(f"{base} pangkat {pangkat} adalah {hasil}")



#Problem 6

def isprime(angka):
    # Bilangan prima harus lebih besar dari 1
    if angka <= 1:
        return False
    
    # 2 dan 3 adalah bilangan prima khusus
    if angka <= 3:
        return True
    
    # Bilangan genap selain 2 bukan bilangan prima
    if angka % 2 == 0:
        return False
    
    # Cek faktor dari 3 hingga akar dari angka
    i = 3
    while i * i <= angka:
        if angka % i == 0:
            return False
        i += 2
    
    return True

#belum selesai, kurang paham untuk full prima nya






