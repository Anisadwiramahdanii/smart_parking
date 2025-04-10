"""
Nama file: main_24782037.py

Deskripsi:
    Modul utama dalam paket 'monitoring' yang berfungsi untuk menerima input
    nomor kendaraan yang akan parkir, memvalidasi nomor tersebut, dan
    menyimpan informasi kendaraan yang terparkir dengan memanfaatkan fungsi
    dari modul 'parking_simulator' dalam paket 'simulator'.

Fitur utama:
    - Menerima input nomor kendaraan dari pengguna.
    - Memvalidasi format nomor kendaraan.
    - Menyimpan informasi kendaraan yang telah divalidasi.

Penulis: Anisa Dwi Ramahdani
Tanggal: 26 Maret 2025
"""

import sys
from os.path import abspath, dirname

# Menambahkan direktori induk ke sys.path untuk memungkinkan impor paket 'simulator'
sys.path.append(dirname(dirname(abspath(__file__))))

from simulator import parking_simulator

def main():
    """
    Fungsi utama yang mengelola proses input, validasi, dan penyimpanan
    nomor kendaraan yang akan parkir.

    Proses:
        1. Meminta input nomor kendaraan dari pengguna.
        2. Memvalidasi format nomor kendaraan menggunakan fungsi
           'validasi_nomor_kendaraan' dari modul 'parking_simulator'.
        3. Jika valid, menyimpan nomor kendaraan menggunakan fungsi
           'simpan_kendaraan_terparkir' dari modul yang sama dan menampilkan
           pesan sukses.
        4. Jika tidak valid, menampilkan pesan kesalahan.

    Parameter:
        Tidak ada.

    Nilai yang dikembalikan:
        Tidak ada.

    Contoh penggunaan:
        Jalankan skrip ini secara langsung. Pengguna akan diminta untuk
        memasukkan nomor kendaraan, dan sistem akan memproses sesuai dengan
        logika yang telah dijelaskan.
    """
    nomor_kendaraan = input("Masukkan nomor kendaraan yang akan parkir: ")
    if parking_simulator.validasi_nomor_kendaraan(nomor_kendaraan):
        parking_simulator.simpan_kendaraan_terparkir(nomor_kendaraan)
        print(f"Kendaraan dengan nomor {nomor_kendaraan} berhasil diparkir.")
    else:
        print("Nomor kendaraan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
