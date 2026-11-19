"""
UTS Dasar Komputer dan Pemrograman
Kelompok C - Instrumentasi
Monitoring Level Tangki
Nama: Ghazal Islamay Subastian

Jalankan:
    python main.py
Pengujian batas:
    python main.py --test
"""

import sys

# 15 data inti dari soal (wajib dipertahankan) + 5 data tambahan.
data_level = [
    18, 25, 33, 41, 55,
    62, 76, 84, 91, 47,
    29, 38, 70, 82, 15,
    29, 30, 80, 81, 50
]


def status_level(level):
    """Mengembalikan status berdasarkan level tangki dalam persen."""
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    else:
        return "HIGH"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori."""
    jumlah = {"LOW": 0, "NORMAL": 0, "HIGH": 0}

    for level in data:
        status = status_level(level)
        jumlah[status] += 1

    return jumlah


def rata_rata(data):
    """Menghitung rata-rata dari sekumpulan angka."""
    return sum(data) / len(data)


def tampilkan_monitoring(data):
    """Menampilkan nilai sensor dan status untuk setiap data."""
    print("===== MONITORING LEVEL TANGKI =====")
    for nomor, level in enumerate(data, start=1):
        status = status_level(level)
        print(f"{nomor:02d}. Level = {level:>3}% -> {status}")


def tampilkan_ringkasan(data):
    """Menampilkan jumlah kategori dan statistik level tangki."""
    jumlah = hitung_kategori(data)

    print("\n===== RINGKASAN =====")
    print(f"Total data       : {len(data)}")
    print(f"Jumlah LOW       : {jumlah['LOW']}")
    print(f"Jumlah NORMAL    : {jumlah['NORMAL']}")
    print(f"Jumlah HIGH      : {jumlah['HIGH']}")
    print(f"Rata-rata level  : {rata_rata(data):.2f}%")
    print(f"Maksimum level   : {max(data)}%")
    print(f"Minimum level    : {min(data)}%")


def jalankan_pengujian():
    """Menguji batas kategori dan nilai minimum/maksimum domain."""
    kasus_uji = [
        (29, "LOW"),       # satu di bawah batas 30
        (30, "NORMAL"),    # tepat pada batas 30
        (31, "NORMAL"),    # satu di atas batas 30
        (79, "NORMAL"),    # satu di bawah batas 80
        (80, "NORMAL"),    # tepat pada batas 80
        (81, "HIGH"),      # satu di atas batas 80
        (0, "LOW"),        # nilai rendah yang valid
        (100, "HIGH")      # nilai tinggi yang valid
    ]

    print("===== TESTING STATUS LEVEL =====")
    semua_lulus = True

    for nomor, (nilai, expected) in enumerate(kasus_uji, start=1):
        actual = status_level(nilai)
        hasil = "PASS" if actual == expected else "FAIL"
        if hasil == "FAIL":
            semua_lulus = False
        print(
            f"Test {nomor}: input={nilai}% | "
            f"expected={expected} | actual={actual} | {hasil}"
        )

    print("Hasil seluruh pengujian:", "PASS" if semua_lulus else "FAIL")


def main():
    tampilkan_monitoring(data_level)
    tampilkan_ringkasan(data_level)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        jalankan_pengujian()
    else:
        main()
