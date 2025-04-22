import streamlit as st

st.title("Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

# Pilih operasi
operasi = st.selectbox(
    "Pilih operasi",
    ("+", "-", "*", "/")
)

# Tombol untuk menghitung
if st.button("Hitung"):
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        hasil = "Operasi tidak valid."

    # Tampilkan hasil
    st.write(f"Hasil: {hasil}")