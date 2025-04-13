# objek kartu isinya pin, informasi, bank

# objek atm isinya objek kartu, bank, pecahan 50/100

import tkinter as tk
from tkinter import messagebox


class Kartu:
    def __init__(self, nomorRekening, bank, saldo):
        self.nomorRekening = nomorRekening
        self.bank = bank
        self.saldo = int(saldo)
    
class KartuATM(Kartu):
    def __init__(self, nomorRekening, bank,  saldo, expired, pin, nama):
        super().__init__(nomorRekening, bank, saldo)
        self.expired = expired
        self.pin = pin
        self.nama = nama
    def autentikasi(self):
        print("\n===================================")
        print("        MASUKKAN PIN ANDA         ")
        print("===================================")
        print("\nPIN harus terdiri dari 6 digit angka.")
    
        inputPin = input("Masukkan PIN: ")
        
        if inputPin == self.pin:
            print("\nPIN diterima!")
            return True
        else:
            print("\nPIN tidak valid! Silakan coba lagi.")
            self.autentikasi()
            return True
    def gantiPin(self):
        print("\n===================================")
        print("        MASUKKAN PIN BARU           ")
        print("===================================")
        print("\nPIN harus terdiri dari 6 digit angka.")
    
        inputPin = input("Masukkan PIN baru: ")
        
        if len(inputPin) != 6:
            print("\nPIN tidak valid! Silakan coba lagi.")
            self.gantiPin()
        elif inputPin == self.pin:
            print("\nPIN sama dengan pin sekarang")
            self.gantiPin()
        else:
            self.pin = inputPin
            print("\nPIN berhasil diganti")
    def informasi(self):
        print("\n====================================")
        print("         INFORMASI REKENING          ")
        print("====================================")
        print ("")
        print("Untuk kembali ke menu utama, ketik 'BACK'")
        print("No. Rekening: ", self.nomorRekening)
        print("Nama Pemilik: ", self.nama)
        print("Bank: ", self.bank)
        print("Expired: ", self.expired)
        print("Saldo: Rp.",self.saldo)
        print("")
        print("====================================")
        
        pilihan = input("Silakan ketik (BACK): ")
        
        if pilihan == "back" or pilihan == "BACK":
            print("\nKembali ke menu utama.")
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
    def transfer (self):
        print("\n====================================")
        print("         TRANSFER UANG              ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print(f"Saldo Anda saat ini: Rp {self.saldo:,}")
        print("")

        nomorRekening = input("Masukkan nomor rekening tujuan: ")
        if nomorRekening == self.nomorRekening:
            print("\nAnda tidak dapat melakukan transfer ke rekening Anda sendiri.")
            return
        jumlah = input("Masukkan jumlah uang: ")
        if jumlah.isdigit():
            jumlah = int(jumlah)

            if jumlah > self.saldo:
                print("\nSaldo tidak mencukupi untuk transfer.")
                return
            elif nomorRekening in self.database_rekening:
                self.saldo -= jumlah  # Saldo pengirim berkurang
                self.database_rekening[nomorRekening] += jumlah  # Saldo penerima bertambah
                print(f"\nTransfer Rp {jumlah:,} ke rekening {nomorRekening} berhasil!")
                print(f"Sisa saldo Anda: Rp {self.saldo:,}")
            else:
                print("\nNomor rekening tujuan tidak ditemukan. Silakan coba lagi.")
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")

class Flazz(Kartu):
    def __init__(self, nomorRekening, bank, saldo):
        super().__init__(nomorRekening, bank, saldo)
        

class ATM:
    def __init__(self,bank, pecahan):
        self.bank = bank
        self.pecahan = pecahan
        # self.kartu = kartu_obj

    # def searchKartu(self): #cari kartu yang ada di txt
        
       

    def tampilkan_kartu(self):
        file = open("kartu.txt", "r")
        list_kartu = []
        dummyIndex = 0
        for line in file: #scan file
            datas = line.strip().split()#di pisah line nya per spasi

            #bikin objek baru pake data di txt
            kartu = KartuATM(datas[0], datas[1], int(datas[2]), datas[3], int(datas[4]), datas[5]) 
            list_kartu.append(kartu)#masukkin objek kartu ke list
        print("==================================")
        print("         SELAMAT DATANG           ")
        print("       DI MESIN ATM INDONESIA     ")
        print("==================================")
        print("")
        print("   ╔═════════════════════════╗")
        print("   ║  pilih kartu            ║")
        print("   ╚═════════════════════════╝")
        print("")
        
        i = 0
        for kartu in (list_kartu):
            print(i+1,".", kartu.nama, "nomor rekening:", kartu.nomorRekening, "bank:", kartu.bank)
            i = i+1
        print("'x' untuk exit" )
        pilihan = input("Pilihan Anda: ")
        if pilihan == "x":
            print("\nTerima kasih! Sampai jumpa lagi.")
        else:
            self.kartu = list_kartu[int(pilihan)-1]
            self.main_menu()

    def pilih_nominal(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.main_menu()
            return
        
        print("\n====================================")
        print("      SILAKAN MEMILIH JUMLAH      ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("")
        print("1. Rp 100.000")
        print("2. Rp 500.000")
        print("3. Rp 1.000.000")
        print("4. Transaksi Lainnya")
        print("")
        print("====================================")
        pilihan = input("Silakan pilih nominal (1/2/3/4): ")
        
        if pilihan == "1":
            print("\nAnda memilih penarikan Rp 100.000.")
            self.tampil_saldo(jumlah=100000)
        elif pilihan == "2":
            print("\nAnda memilih penarikan Rp 500.000.")
            self.tampil_saldo(jumlah=500000)
        elif pilihan == "3":
            print("\nAnda memilih penarikan Rp 1.000.000.")
            self.tampil_saldo(jumlah=1000000)
        elif pilihan == "4":
            print("\nAnda memilih 'Transaksi Lainnya'. Silakan pilih layanan tambahan.")
            self.main_menu()
        elif pilihan == "CANCEL" or pilihan == "cancel":
            print("\nTransaksi dibatalkan.")
            self.tampilkan_pesan() 
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pilih_nominal()
    def main_menu(self):
        print("\n====================================")
        print("        PILIH TRANSAKSI LAINNYA     ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("1. Informasi") 
        print("2. Penarikan Tunai")
        print("3. Transfer") 
        print("4. Pembayaran") #belum
        print("5. Ganti PIN")
        print("6. Flazz")#belum
        print("7. Setor Tunai") 
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih layanan (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            print("\nAnda memilih INFORMASI. Menampilkan informasi rekening...")
            self.kartu.informasi()
            self.main_menu() 
        elif pilihan == "2":
            print("\nAnda memilih PENARIKAN TUNAI. Silakan pilih jumlah uang.")
            self.pilih_pecahan() 
        elif pilihan == "3":
            print("\nAnda memilih TRANSFER. Silakan masukkan nomor rekening tujuan.")
            self.kartu.transfer()
            self .main_menu()
        elif pilihan == "4":
            print("\nAnda memilih PEMBAYARAN. Silakan pilih jenis pembayaran.")
            self.pembayaran()
        elif pilihan == "5":
            print("\nAnda memilih GANTI PIN. Silakan masukkan PIN baru.")
            self.kartu.gantiPin()
            self.tampilkan_pesan()
        elif pilihan == "6":
            print("\nAnda memilih FLazz. Silakan pilih fitur kartu Flazz.")
            self.kartu.flazz()
            self.main_menu()
        elif pilihan == "7":
            print("\nAnda memilih SETOR TUNAI. Silakan masukkan uang ke mesin.")
            self.setor_tunai()
        elif pilihan == "cancel" or pilihan == "CANCEL":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.tampilkan_pesan()
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.main_menu()

    def pilih_pecahan(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.main_menu()
            return
        
        print("\n====================================")
        print("   SILAKAN MEMILIH PECAHAN UANG    ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("")
        print("1. Rp 50.000")
        print("2. Rp 100.000")
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih pecahan uang (1/2): ").lower()
        
        if pilihan == "1":
            print("\nAnda memilih pecahan Rp 50.000.")
            self.masukkan_jumlah_uang()
        elif pilihan == "2":
            print("\nAnda memilih pecahan Rp 100.000.")
            self.masukkan_jumlah_uang()
        elif pilihan == "cancel" or pilihan == "CANCEL":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.tampilkan_pesan()
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pilih_pecahan() 
            
    def masukkan_jumlah_uang(self):
        print("\n====================================")
        print("   MASUKKAN JUMLAH UANG YANG DIINGINKAN   ")
        print("====================================")
        print("Untuk membatalkan transaksi, tekan 'CANCEL'")
        print("")
        
        jumlah = input("Masukkan jumlah penarikan: ").replace(".", "").strip()

        if jumlah == "cancel":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.tampilkan_pesan()
        elif jumlah.isdigit():
            jumlah = int(jumlah)
            if jumlah % 50000 == 0 and jumlah >= 50000:  # Memastikan nominal bulat kelipatan 50.000
                self.tampil_saldo(jumlah)
            else:
                print("\nNominal tidak valid! Masukkan kelipatan Rp 50.000.")
                self.masukkan_jumlah_uang()  
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.masukkan_jumlah_uang()

    def tampil_saldo(self, jumlah):
        if self.kartu.saldo <= 0 or jumlah > self.kartu.saldo:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.main_menu()
            return

        print("\n====================================")
        print(" APAKAH ANDA INGIN MAMPILKAN SALDO?   ")
        print("====================================")
        print("")
        print("1. Tampil Saldo")
        print("2. Tidak Tampil Saldo")
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih (1/2): ")
        
        if pilihan == "1":
            saldo = self.kartu.saldo
            print("\nMenampilkan saldo...")
            print("\n====================================") 
            print(f"Saldo Anda saat ini: Rp {saldo:,}")
            print("====================================") 
            print("")
            print(f"Anda akan menarik Rp {jumlah:,} Silakan ambil uang Anda.")
            self.kartu.saldo = self.kartu.saldo - jumlah
            print("Saldo anda sekarang" + str(self.kartu.saldo))
            self.selesai_transaksi()
        elif pilihan == "2":
            print(f"\nAnda akan menarik Rp {jumlah:,} Silakan ambil uang Anda.")
            self.kartu.saldo = self.kartu.saldo - jumlah
            self.selesai_transaksi()
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.tampil_saldo()
    def selesai_transaksi(self):
        print("\n================================================")
        print("APAKAH ANDA INGIN MELAKUKAN TRANSAKSI LAINNYA?")
        print("================================================")
        print("")
        print("1. Ya")
        print("2. Tidak")
        print("")
        print("================================================")
        pilihan = input ("Silakan pilih (1/2): ")
        if pilihan == "1":
            self.main_menu()
        elif pilihan == "2":
            print("\nTransaksi Selesai. Terima kasih telah menggunakan layanan kami.")
    def setor_tunai(self):
        print("\n====================================")
        print("         SETOR TUNAI                 ")
        print("====================================")
        print("masukkan jumlah uang yang ingin di setor")
        
        pilihan = input("Jumlah uang: ")    
        self.kartu.saldo += int(pilihan)
    def pembayaran(self):
        print("\n====================================")
        print("         PEMBAYARAN TAGIHAN        ")
        print("1. Listrik                          ")
        print("2. Kredit                           ")
        print("3. Air                              ")
        print("4. Paylater                         ")
        print("====================================")
    
        pilihan = input("Silakan pilih (1/2/3/4): ")
        
    
        if pilihan == '1':
            jenis_tagihan = "listrik"
        elif pilihan == '2':
            jenis_tagihan = "kredit"
        elif pilihan == '3':
            jenis_tagihan = "air"
        elif pilihan == '4':
            jenis_tagihan = "paylater"
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pembayaran() 
            return 
        
        jumlah_tagihan = input("Jumlah tagihan: ")
        
        if not jumlah_tagihan.isdigit():
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pembayaran()  
            return
    
        jumlah_tagihan = int(jumlah_tagihan)

        if jumlah_tagihan > self.kartu.saldo:
            print("\nSaldo tidak mencukupi untuk melakukan pembayaran.")
            self.main_menu() 
        else:
            self.kartu.saldo -= jumlah_tagihan
            print(f"\nPembayaran tagihan {jenis_tagihan} sebesar Rp {jumlah_tagihan:,} berhasil!")
            print(f"Sisa saldo Anda: Rp {self.kartu.saldo:,}")
            self.selesai_transaksi()  
#objek atm

# class GUIatm(ATM):
#     def __init__(self, atm):
#         self.atm = atm
#         self.window = tk.Tk()
#         self.window.title("ATM Machine")

#         self.label = tk.Label(self.window, text="Selamat Datang di ATM!")
#         self.label.pack()

#         self.pin_label = tk.Label(self.window, text="Masukkan PIN:")
#         self.pin_label.pack()
#         self.pin_entry = tk.Entry(self.window, show="*")
#         self.pin_entry.pack()

#         self.login_button = tk.Button(self.window, text="Login", command=self.login)
#         self.login_button.pack()

#         self.result_label = tk.Label(self.window, text="")
#         self.result_label.pack()


# kartu1 = KartuATM("1234567890", "BCA",  2000000, "12/25" ,"123456", "Jon Doaa")  

atm1 = ATM("BCA", 50000 or 100000)

atm1.tampilkan_kartu()