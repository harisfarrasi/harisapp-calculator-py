try:
    angka1_str = input("Masukkan angka pertama: ")
    angka2_str = input("Masukkan angka kedua: ")
    operasi = input("Masukkan operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = int(angka1_str) + int(angka2_str)
    elif operasi == "-":
        hasil = int(angka1_str) - int(angka2_str)
    elif operasi == "*":
        hasil = int(angka1_str) * int(angka2_str)
    elif operasi == "/":
        hasil = int(angka1_str) / int(angka2_str)
    else:
        print("Operasi tidak valid. Silakan masukkan salah satu dari +, -, *, /")
        exit()
    
    print(f"Hasil: {hasil}")

except ValueError:
    print("Input tidak valid. Silakan masukkan angka.")