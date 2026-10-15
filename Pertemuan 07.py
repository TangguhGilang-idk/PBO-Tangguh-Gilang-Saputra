import datetime
import json
import time
import builtins

print = builtins.print


def judul(teks):
    print("\n" + "=" * 60)
    print(teks)
    print("=" * 60)


def pengenalan_modul():
    judul("1. PENGENALAN MODUL datetime DAN time")
    print("datetime : date, time, datetime, timedelta")
    print("time     : time(), sleep(), localtime(), strftime(), dll.")


def buat_dan_manipulasi():
    judul("2. PEMBUATAN & MANIPULASI OBJEK TANGGAL DAN WAKTU")

    tgl = datetime.date(2026, 10, 15)
    wkt = datetime.time(17, 57, 26)
    dt = datetime.datetime(2026, 10, 15, 17, 57, 26)
    print("date     :", tgl)
    print("time     :", wkt)
    print("datetime :", dt)

    print("\nTahun:", dt.year, "| Bulan:", dt.month, "| Hari:", dt.day)
    print("Jam  :", dt.hour, "| Menit:", dt.minute, "| Detik:", dt.second)

    print("\nBesok           :", dt + datetime.timedelta(days=1))
    print("2 jam yang lalu :", dt - datetime.timedelta(hours=2))
    print("Selisih ke 31-12-2026:", (datetime.date(2026, 12, 31) - tgl).days, "hari")
    print("Replace tahun 2030   :", dt.replace(year=2030))


def waktu_saat_ini():
    judul("3. CURRENT DATE, CURRENT DATETIME, CURRENT TIME")

    current_date = datetime.date.today()
    current_datetime = datetime.datetime.now()
    current_time = datetime.datetime.now().time()

    print("Current date     :", current_date)
    print("Current datetime :", current_datetime)
    print("Current time     :", current_time)


def demo_strftime():
    judul("4. strftime() : DATETIME -> STRING")

    sekarang = datetime.datetime.now()
    print("DD-MM-YYYY :", sekarang.strftime("%d-%m-%Y"))
    print("Jam 24     :", sekarang.strftime("%H:%M:%S"))
    print("Jam 12     :", sekarang.strftime("%I:%M:%S %p"))
    print("Lengkap    :", sekarang.strftime("%A, %d %B %Y %H:%M:%S"))


def demo_strptime():
    judul("5. strptime() : STRING -> DATETIME")

    teks = "25-12-2026 14:30:00"
    hasil = datetime.datetime.strptime(teks, "%d-%m-%Y %H:%M:%S")
    print("String   :", teks)
    print("Datetime :", hasil, type(hasil))

    print("Bulan    :", hasil.month, "| Jam:", hasil.hour)
    print("Selisih dengan sekarang:", hasil - datetime.datetime.now())


def demo_timestamp():
    judul("6. UNIX TIMESTAMP")

    ts = time.time()
    print("Timestamp sekarang :", ts)

    print("Timestamp -> datetime :", datetime.datetime.fromtimestamp(ts))

    dt = datetime.datetime(2026, 1, 1, 0, 0, 0)
    print("Datetime -> timestamp :", dt.timestamp())

    data = {"event": "login", "waktu": int(ts)}
    teks_json = json.dumps(data)
    print("\nData disimpan (JSON)  :", teks_json)

    diterima = json.loads(teks_json)
    waktu_asli = datetime.datetime.fromtimestamp(diterima["waktu"])
    print("Data dibaca kembali   :", waktu_asli.strftime("%d-%m-%Y %H:%M:%S"))


def demo_sleep():
    judul("7. time.sleep()")

    print("Loading sistem", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" selesai!")

    print("\nMengukur delay program:")
    mulai = time.time()
    time.sleep(2)
    print(f"Program ditunda selama {time.time() - mulai:.2f} detik")

    print("\nProgress:")
    for i in range(0, 101, 25):
        print(f"[{'#' * (i // 5):<20}] {i}%")
        time.sleep(0.5)


def catat_aktivitas(daftar_log, aktivitas):
    """Mencatat aktivitas beserta waktunya."""
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    daftar_log.append(f"[{waktu}] {aktivitas}")


def studi_kasus_log():
    judul("8a. STUDI KASUS: PENCATATAN AKTIVITAS")

    log = []
    catat_aktivitas(log, "User login")
    time.sleep(1)
    catat_aktivitas(log, "Membuka dashboard")
    time.sleep(1)
    catat_aktivitas(log, "User logout")

    for baris in log:
        print(baris)


def studi_kasus_monitoring(jumlah=5, interval=1):
    judul("8b. STUDI KASUS: MONITORING SISTEM")

    mulai = datetime.datetime.now()
    for i in range(1, jumlah + 1):
        sekarang = datetime.datetime.now()
        uptime = (sekarang - mulai).seconds
        print(f"Cek #{i} | {sekarang.strftime('%H:%M:%S')} | uptime: {uptime} detik | status: OK")
        time.sleep(interval)

def main():
    pengenalan_modul()
    buat_dan_manipulasi()
    waktu_saat_ini()
    demo_strftime()
    demo_strptime()
    demo_timestamp()
    demo_sleep()
    studi_kasus_log()
    studi_kasus_monitoring()


if __name__ == "__main__":
    main()
