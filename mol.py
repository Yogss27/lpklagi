import streamlit as st
import math

def molarity_to_ph(molarity):
    # Konstanta ionisasi asam
    Ka = 1.8e-5

    # Menghitung pH berdasarkan konsentrasi molaritas
    pH = -math.log10(math.sqrt(Ka * molarity))

    return pH

def neutralization_concentration(volume_a, concentration_a, volume_b, concentration_b):
    # Menghitung konsentrasi setelah netralisasi
    concentration_final = (volume_a * concentration_a + volume_b * concentration_b) / (volume_a + volume_b)

    return concentration_final

# Judul aplikasi
st.title("Kalkulator Molaritas ke pH")

# Input konsentrasi molaritas
molarity = st.number_input("Masukkan konsentrasi molaritas (mol/L):", min_value=0.0)

# Konversi molaritas ke pH
if molarity:
    pH_result = molarity_to_ph(molarity)
    st.write("pH:", pH_result)

# Input parameter netralisasi
st.header("Netralisasi")
volume_a = st.number_input("Masukkan volume larutan A (mL):", min_value=0.0)
concentration_a = st.number_input("Masukkan konsentrasi larutan A (mol/L):", min_value=0.0)
volume_b = st.number_input("Masukkan volume larutan B (mL):", min_value=0.0)
concentration_b = st.number_input("Masukkan konsentrasi larutan B (mol/L):", min_value=0.0)

# Menghitung konsentrasi setelah netralisasi
if volume_a and concentration_a and volume_b and concentration_b:
    concentration_final = neutralization_concentration(volume_a, concentration_a, volume_b, concentration_b)
    st.write("Konsentrasi setelah netralisasi:", concentration_final)
