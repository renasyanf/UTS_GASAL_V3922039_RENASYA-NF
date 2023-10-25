# Fungsi untuk mencari invers modulo dari a terhadap m
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk melakukan enkripsi menggunakan Affine Cipher
def affine_encrypt(plain_text, key_a, key_b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A')  # Mendapatkan indeks karakter (A=0, B=1, ...)
            encrypted_idx = (key_a * char_idx + key_b) % 26  # Rumus enkripsi Affine
            encrypted_char = chr(encrypted_idx + ord('A'))  # Mengonversi indeks kembali ke karakter
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk melakukan dekripsi menggunakan Affine Cipher
def affine_decrypt(encrypted_text, key_a, key_b):
    key_a_inv = mod_inverse(key_a, 26)  # Menghitung invers modulo untuk kunci a
    if key_a_inv is None:
        return "Kunci tidak valid."

    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A')  # Mendapatkan indeks karakter (A=0, B=1, ...)
            decrypted_idx = (key_a_inv * (char_idx - key_b)) % 26  # Rumus dekripsi Affine
            decrypted_char = chr(decrypted_idx + ord('A'))  # Mengonversi indeks kembali ke karakter
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk melakukan enkripsi menggunakan Vigenère Cipher
def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()  # Mengonversi teks masukan dan kunci menjadi huruf kapital
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char.isalpha():
            key_char = key[i % key_length]  # Mengambil karakter kunci yang sesuai
            shift = ord(key_char) - ord('A')  # Menghitung pergeseran berdasarkan karakter kunci
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))  # Rumus enkripsi Vigenère
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk melakukan dekripsi menggunakan Vigenère Cipher
def vigenere_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()  # Mengonversi teks terenkripsi dan kunci menjadi huruf kapital
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            key_char = key[i % key_length]  # Mengambil karakter kunci yang sesuai
            shift = ord(key_char) - ord('A')  # Menghitung pergeseran berdasarkan karakter kunci
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))  # Rumus dekripsi Vigenère
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi utama program
def main():
    print("UTS ENKRIPSI DAN DESKRIPSI")

    while True:
        choice = input("Pilih metode:\nA. Affine Cipher\nV. Vigenère Cipher\nPilihan (A/V): ")
        
        if choice not in ['A', 'V']:
            print("Pilihan tidak valid. Silakan pilih 'A' untuk Affine atau 'V' untuk Vigenère.")
            continue

        if choice == 'A':
            key_a = int(input("Masukkan nilai kunci a : "))
            key_b = int(input("Masukkan nilai kunci b : "))
            plain_text = input("Masukkan teks yang ingin dienkripsi: ")
            encrypted_text = affine_encrypt(plain_text, key_a, key_b)
        else:
            key = input("Masukkan kunci Vigenère: ")
            plain_text = input("Masukkan teks yang akan dienkripsi: ")
            encrypted_text = vigenere_encrypt(plain_text, key)

        decrypted_text = ""
        if choice == 'A':
            decrypted_text = affine_decrypt(encrypted_text, key_a, key_b)
        else:
            decrypted_text = vigenere_decrypt(encrypted_text, key)
        
        print("Teks terenkripsi:", encrypted_text)
        print("Teks terdekripsi:", decrypted_text)
        
        another = input("Lakukan operasi lainnya? (yes/no): ")
        if another.lower() != 'y':
            break

if _name_ == "_main_":
    main()