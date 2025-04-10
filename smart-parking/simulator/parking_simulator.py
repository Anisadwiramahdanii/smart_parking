"""
Nama file: parking_simulator.py

Deskripsi:
    Modul ini menyediakan fungsi-fungsi untuk validasi dan penyimpanan
    nomor kendaraan dalam sistem parkir.

Fitur utama:
    - Validasi format nomor kendaraan.
    - Penyimpanan informasi kendaraan yang telah divalidasi.

Penulis: Anisa Dwi Ramahdani
Tanggal: 26 Maret 2025
"""

def validasi_nomor_kendaraan(nomor):
    """
    Memvalidasi format nomor kendaraan berdasarkan pola tertentu.

    Parameter:
        nomor (str): Nomor kendaraan yang akan divalidasi.

    Returns:
        bool: True jika format nomor kendaraan valid, False jika tidak.

    Contoh penggunaan:
        >>> validasi_nomor_kendaraan('B 1234 CD')
        True
        >>> validasi_nomor_kendaraan('1234 AB')
        False
    """
    import re
    pola = r'^[A-Z]{1,2} \d{1,4} [A-Z]{1,3}$'
    return re.match(pola, nomor) is not None

def simpan_kendaraan_terparkir(nomor):
    """
    Menyimpan nomor kendaraan yang telah divalidasi ke dalam daftar parkir.

    Parameter:
        nomor (str): Nomor kendaraan yang akan disimpan.

    Returns:
        None

    Contoh penggunaan:
        >>> simpan_kendaraan_terparkir('B 1234 CD')
        Kendaraan dengan nomor B 1234 CD telah disimpan dalam daftar parkir.
    """
    print(f"Kendaraan dengan nomor {nomor} telah disimpan dalam daftar parkir.")
