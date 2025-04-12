# objek kartu isinya pin, informasi, bank

# objek atm isinya objek kartu, bank, pecahan 50/100


class Kartu:
    def __init__(self, pin, nama, nomorRekening, bank, expired, saldo,):
        self.pin = pin
        self.nama = nama
        self.nomorRekening = nomorRekening
        self.bank = bank
        self.expired = expired
        self.saldo = saldo
        self.database_rekening = {
            "1234567890": 500000,  # Rekening tujuan pertama
            "1233567890": 1000000,  # Rekening tujuan kedua
        }

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
class ATM:
    def __init__(self,bank, pecahan, kartu_obj):
        self.bank = bank
        self.pecahan = pecahan
        self.kartu = kartu_obj

    def tampilkan_pesan(self):
        print("==================================")
        print("         SELAMAT DATANG           ")
        print("       DI MESIN ATM INDONESIA     ")
        print("==================================")
        print("")
        print("   ╔═════════════════════════╗")
        print("   ║  Apakah ingin           ║")
        print("   ║  memasukkan kartu? (y/n)║")
        print("   ╚═════════════════════════╝")
        print("")
        
        pilihan = input("Pilihan Anda: ").lower()
        if pilihan == "y":
            if self.kartu.autentikasi() == True:
                self.transaksi_lainnya()
        elif pilihan == "n":
            print("\nTerima kasih! Sampai jumpa lagi.")
        else:
            print("\nMasukan tidak valid, coba lagi.")
    def pilih_nominal(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.transaksi_lainnya()
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
            self.transaksi_lainnya()
        elif pilihan == "CANCEL" or pilihan == "cancel":
            print("\nTransaksi dibatalkan.")
            self.tampilkan_pesan() 
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pilih_nominal()
    def transaksi_lainnya(self):
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
        print("7. Setor Tunai") #belum
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih layanan (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            print("\nAnda memilih INFORMASI. Menampilkan informasi rekening...")
            self.kartu.informasi()
            self.transaksi_lainnya() 
        elif pilihan == "2":
            print("\nAnda memilih PENARIKAN TUNAI. Silakan pilih jumlah uang.")
            self.pilih_pecahan() 
        elif pilihan == "3":
            print("\nAnda memilih TRANSFER. Silakan masukkan nomor rekening tujuan.")
            self.kartu.transfer()
            self .transaksi_lainnya()
        elif pilihan == "4":
            print("\nAnda memilih PEMBAYARAN. Silakan pilih jenis pembayaran.")
        elif pilihan == "5":
            print("\nAnda memilih GANTI PIN. Silakan masukkan PIN baru.")
            self.kartu.gantiPin()
            self.tampilkan_pesan()
        elif pilihan == "6":
            print("\nAnda memilih FLazz. Silakan pilih fitur kartu Flazz.")
            self.kartu.flazz()
            self.transaksi_lainnya()
        elif pilihan == "7":
            print("\nAnda memilih SETOR TUNAI. Silakan masukkan uang ke mesin.")
            self.setor_tunai()
        elif pilihan == "cancel" or pilihan == "CANCEL":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.tampilkan_pesan()
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.transaksi_lainnya()

    def pilih_pecahan(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.transaksi_lainnya()
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
        
        jumlah = input("Masukkan jumlah penarikan: ").lower().replace(".", "").strip()

        if jumlah == "cancel" or jumlah == "CANCEL":
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
            self.transaksi_lainnya()
        elif pilihan == "2":
            print("\nTransaksi Selesai. Terima kasih telah menggunakan layanan kami.")


#objek atm
kartu1 = Kartu("123456", "John Doe", "1234567890", "BCA", "12/25", 2000000,)  
atm1 = ATM("BCA", 50000 or 100000, kartu1)
kartu2 = Kartu("888888", "John dick", "1233567890", "BRI", "12/25", 1000000,)
atm1.tampilkan_pesan()