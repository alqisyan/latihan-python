from datetime import time

JAM_SIANG = 100000
JAM_MALAM = 150000
FOTO_SIANG = 150000
FOTO_MALAM = 200000
ROMPI = 5000

def login():
    login = 3
    while True:
        username = input("Masukkan Username")
        password = input("Masukkan Password")
        if username == "FutsalUser" and password == "futsal123":
            break
        else:
            print("Username dan Password tidak sesuai")
            # login -= 1
            # if login >= 0:
            #     print("Anda telah salah mengisikan akun, tunggu 10 detik untuk kembali")

def sewa():
    jam_sewa = input('Enter a time in the format HH:MM \n')
    durasi = int(input("Masukkan Durasi sewa"))
    if jam_sewa >= "00:00" and jam_sewa <= "06:00":
        print("Futsal masih tutup")
    elif jam_sewa >= "06:00" and jam_sewa <= "17:00":
        #print( 100000 * durasi)
        return JAM_SIANG * durasi
    elif jam_sewa >= "18:00" and jam_sewa <= "00:00" :
        #print( 150000 * durasi)
        return JAM_MALAM * durasi

def fotografer():
    jam_pakai = input('Enter a time in the format HH:MM \n')
    durasi = int(input("Masukkan Durasi sewa"))
    if jam_pakai >= "00:00" and jam_pakai <= "06:00":
        print("Futsal masih tutup")
    elif jam_pakai >= "06:00" and jam_pakai <= "17:00":
        #print( 100000 * durasi)
        return FOTO_SIANG * durasi
    elif jam_pakai >= "18:00" and jam_pakai <= "00:00" :
        #print( 150000 * durasi)
        return FOTO_MALAM * durasi

def rompi():
    lama_sewa = int(input("Masukkan Durasi sewa : "))
    banyak_sewa =  int(input("Masukkan jumlah rompi yang mau di sewa"))
    if banyak_sewa >= 4 :
        return banyak_sewa * (lama_sewa * ROMPI)
    else:
        print("Pesan rompi minimal 4")

def main():
    #login()
    print("Selamat Datang")
    biayaSewa = sewa()
    biayaFoto = fotografer()
    biayaRompi = rompi()
    total = biayaSewa + biayaFoto + biayaRompi
    print(total)

main()