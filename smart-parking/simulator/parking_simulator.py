# simulator/parking_simulator.py

parkiran = []


def tambah_slot_parkir(jumlah):
    """
    Menambahkan sejumlah slot parkir kosong.
    """
    global parkiran
    parkiran.extend([None] * jumlah)
    print(f"{jumlah} slot parkir berhasil ditambahkan.")


def parkir_kendaraan(nomor):
    """
    Memarkir kendaraan ke slot kosong pertama.
    """
    for i in range(len(parkiran)):
        if parkiran[i] is None:
            parkiran[i] = nomor
            print(f"Kendaraan {nomor} diparkir di slot {i + 1}.")
            return
    print("Maaf, semua slot penuh.")


def kendaraan_keluar(nomor):
    """
    Mengeluarkan kendaraan dari slot jika ditemukan.
    """
    for i in range(len(parkiran)):
        if parkiran[i] == nomor:
            parkiran[i] = None
            print(f"Kendaraan {nomor} keluar dari slot {i + 1}.")
            return
    print(f"Kendaraan {nomor} tidak ditemukan.")


def cek_status_parkir():
    """
    Menampilkan status semua slot parkir.
    """
    print("\nStatus Parkir:")
    for i, kendaraan in enumerate(parkiran):
        status = kendaraan if kendaraan else "Kosong"
        print(f"Slot {i + 1}: {status}")
