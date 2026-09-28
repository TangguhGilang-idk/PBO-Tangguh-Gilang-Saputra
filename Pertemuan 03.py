#Sistem Pendataan Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def cetak_profil(self):
        print(f"NIM: {self.nim} | Nama: {self.nama} | Jurusan: {self.jurusan} | Status: {self.cek_status()}")

mhs1 = Mahasiswa("Ubed", "2595114037", "Teknik Informatika", 89)
mhs2 = Mahasiswa("Gilang", "2595114026", "Teknik Informatika", 71)
mhs3 = Mahasiswa("Fuad", "2595114030", "Teknik Informatika", 75)

print("=== Profil Data Mahasiswa ===")
mhs1.cetak_profil()
mhs2.cetak_profil()
mhs3.cetak_profil()

#Sistem Rental Kendaraan
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info_dasar(self):
        return f"{self.nama} ({self.merk}, {self.tahun}) - {self.kecepatan} km/h"

class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def info_mobil(self):
        return f"[MOBIL] {self.info_dasar()} | Jumlah Kursi: {self.jumlah_kursi}"

class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def info_motor(self):
        return f"[MOTOR] {self.info_dasar()} | Tipe: {self.tipe_motor}"

mobil1 = Mobil("Avanza", "Toyota", 2022, 120, 7)
motor1 = Motor("Beat", "Honda", 2021, 100, "Matic")

print("=== Info Kendaraan ===")
print(mobil1.info_mobil())
print(motor1.info_motor())

#Sistem Manajemen Pegawai
class IdentitasPegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama

class Penggajian:
    def __init__(self, gaji):
        self.gaji = gaji

class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

class ProjectManager(IdentitasPegawai, Penggajian, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        IdentitasPegawai.__init__(self, id_pegawai, nama)
        Penggajian.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_profil(self):
        print("=== Profil Project Manager ===")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Nama Lengkap : {self.nama}")
        print(f"Gaji         : Rp {self.gaji:,}")
        print(f"Tanggung Jawab Proyek : {self.nama_proyek}")

pm1 = ProjectManager("25170", "Tangguh Gilang", 15000000, "Sistem IT Rumah Sakit")
pm1.tampilkan_profil()