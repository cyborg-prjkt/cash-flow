import os
from datetime import datetime
from time import sleep

tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

logo_dashboard =[r"""
   _________ ______/ /_     / __/ /___ _      __
  / ___/ __ `/ ___/ __ \   / /_/ / __ \ | /| / /
 / /__/ /_/ (__  ) / / /  / __/ / /_/ / |/ |/ / 
 \___/\__,_/____/_/ /_/  /_/ /_/\____/|__/|__/  
"""]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# membuat file
with open("keuangan.txt", "a") as f:
    f.write("")
with open("uang.txt", "a") as f:
    f.write("")
# saldo
try:
    with open("uang.txt", "r") as f:
        isi = f.read().strip()
        uang = int(isi) if isi else 0
except (FileNotFoundError, ValueError):
    uang = 0

def cash_flow_dashboard(uang):
    clear()
    print(logo_dashboard[0])
    print("-" * 75)
    print(" Dashboard".center(70))
    print("-" * 75)
    print(f" Saldo anda saat ini: Rp.{uang}")
    print("-" * 75)
    print(" 1. Pemasukan")
    print(" 2. Pengeluaran")
    print(" 3. lihat laporan keuangan")
    print("-" * 75)
    menu = input(" pilih menu: ")
    if menu == "1":
        pemasukan(uang)
    elif menu == "2":
        pengeluaran(uang)
    elif menu == "3":
        laporan_keuangan()
    else:
        print()
        print(" menu tidak tersedia")
        sleep(2)
        cash_flow_dashboard(uang)

def pemasukan(uang):
    clear()
    print(logo_dashboard[0])
    print("-"* 75)
    print(" Pemasukan".center(70))
    print("-"* 75)
    uang_masuk = input(" masukkan jumlah uang masuk: Rp.")
    sumber_uang = input(" masukkan sumber uang masuk: ")
    with open("keuangan.txt", "a") as file:
        file.write(f"""
 ---------------------------------------
            Pemasukan
 ---------------------------------------
 Jumlah uang masuk : {uang_masuk},
 sumber uang masuk : {sumber_uang},
 tanggal uang masuk: {tanggal},
 ---------------------------------------
\n""")
    uang = int(uang) + int(uang_masuk)
    with open("uang.txt", "w") as f:
        f.write(str(uang))
    print()
    print(" Data pemasukan berhasil disimpan.")
    sleep(2)
    cash_flow_dashboard(uang)

def pengeluaran(uang):
    clear()
    print(logo_dashboard[0])
    print("-"* 75)
    print(" Pengeluaran".center(70))
    print("-"* 75)
    uang_keluar = input(" masukkan jumlah uang keluar: Rp.")
    keterangan = input(" keterangan uang yang keluar: ")
    with open("keuangan.txt", "a") as file:
        file.write(f"""
 ---------------------------------------
             Pengeluaran
 ---------------------------------------
 Jumlah uang keluar : {uang_keluar},
 keterangan uang keluar : {keterangan},
 tanggal uang keluar: {tanggal},
 ---------------------------------------
\n""")
    if int(uang_keluar) > int(uang):
        print()
        print(" Saldo anda tidak mencukupi untuk melakukan pengeluaran ini.")
        sleep(2)
        cash_flow_dashboard(uang)
    else:
        uang = int(uang) - int(uang_keluar)
        with open("uang.txt", "w") as f:
            f.write(str(uang))
        print()
        print(" Data pengeluaran berhasil disimpan.")
        sleep(2)
        cash_flow_dashboard(uang)

def laporan_keuangan():
    clear()
    print(logo_dashboard[0])
    print("-"* 75)
    print(" Laporan Keuangan".center(70))
    print("-"* 75)
    print()
    with open("keuangan.txt", "r") as file:
        laporan = file.read()
    if laporan == "":
        print(" Belum ada data keuangan yang tercatat.")
    else:
        print(" Berikut adalah laporan keuangan Anda:")
        print(laporan)
    print()
    input(" Tekan Enter untuk kembali ke dashboard...")
    cash_flow_dashboard(uang)

if __name__ == "__main__":
    cash_flow_dashboard(uang)