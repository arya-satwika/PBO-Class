# objek kartu isinya pin, informasi, bank

# objek atm isinya objek kartu, bank, pecahan 50/100


from abc import ABC, abstractmethod

class Kartu:
    def __init__(self, nomorRekening, bank, saldo):
        self.nomorRekening = nomorRekening
        self.bank = bank
        self.saldo = int(saldo)
    @abstractmethod
    def informasi(self):
        pass
    
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

        dummyIndex = 1
        for kartu in list_kartu_atm:
            print(dummyIndex,". Nomor: ", kartu.nomorRekening, "Bank: ", kartu.bank, "Saldo: ", kartu.saldo)
            dummyIndex = dummyIndex + 1
        selected = input("Masukan nomor kartu tujuan: ")
        self.Kartu = list_kartu_atm[int(selected)-1]
        if self.Kartu == self:
            print("\nAnda tidak dapat melakukan transfer ke rekening Anda sendiri.")
            return
        jumlah_transfer = input("Masukkan jumlah transfer: ").strip()
        if jumlah_transfer.lower() == "cancel":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.menu_atm()
            return
        
        if not jumlah_transfer.isdigit():
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.transfer()
            return
        
        jumlah_transfer = int(jumlah_transfer)
        
        if self.saldo < jumlah_transfer:
            print("\nTransfer gagal! Saldo Anda tidak mencukupi, Silahkan Liat Saldo Anda Lagi.")
            self.transfer()
        else:
            self.saldo = self.saldo - jumlah_transfer
            self.Kartu.saldo = self.Kartu.saldo + jumlah_transfer
            print(f"\nTransfer Rp {jumlah_transfer:,} berhasil!")
            print(f"Sisa saldo Anda: Rp {self.saldo:,}")
    def main_menu(self):
        print("\n====================================")
        print("        PILIH TRANSAKSI LAINNYA     ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("1. Informasi") 
        print("2. Penarikan Tunai")
        print("3. Transfer") 
        print("4. Pembayaran") 
        print("5. Ganti PIN")
        print("6. Flazz")
        print("7. Setor Tunai")
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih layanan (1/2/3/4/5/6/7): ")
        return pilihan
        

class Flazz(Kartu):
    def __init__(self, nomorRekening, bank, saldo):
        super().__init__(nomorRekening, bank, saldo)
    def informasi(self):
        print("\n====================================")
        print("         INFORMASI REKENING          ")
        print("====================================")
        print ("")
        print("Untuk kembali ke menu utama, ketik 'BACK'")
        print("No. Kartu: ", self.nomorRekening)
        print("Bank: ", self.bank)
        print("Saldo: Rp.",self.saldo)
        print("")
        print("====================================")
        
        pilihan = input("Silakan ketik (BACK): ")
        
        if pilihan == "back" or pilihan == "BACK":
            print("\nKembali ke menu utama.")
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
    def main_menu(self):
        print("\n====================================")
        print("        PILIH TRANSAKSI LAINNYA     ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("1. Informasi") 
        print("2. Top Up")
        print("")
        print("====================================")
        
        pilihan = input("Silakan pilih layanan (1/2): ")
        return pilihan

class ATM:
    def __init__(self,bank, pecahan):
        self.bank = bank
        self.pecahan = pecahan
        
        

    def tampilkan_kartu(self):
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
        for kartu in (list_kartu_atm):
            print(i+1,".", kartu.nama, "nomor rekening:", kartu.nomorRekening, "bank:", kartu.bank)
            i = i+1
        print("'x' untuk exit" )
        pilihan = input("Pilihan Anda: ")
        if pilihan == "x":
            print("\nTerima kasih! Sampai jumpa lagi.")
        else:
            self.kartu = list_kartu_atm[int(pilihan)-1]
            self.kartu.autentikasi()
            self.menu_atm()

    def pilih_nominal(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.menu_atm()
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
            self.menu_atm()
        elif pilihan == "CANCEL" or pilihan == "cancel":
            print("\nTransaksi dibatalkan.")
            self.tampilkan_pesan() 
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.pilih_nominal()
    def menu_kartu(self, kartu):
        choice = kartu.main_menu()
        return choice 
    def menu_atm(self):
        pilihan = self.menu_kartu(self.kartu)
        
        if pilihan == "1":
            print("\nAnda memilih INFORMASI. Menampilkan informasi rekening...")
            self.kartu.informasi()
            self.menu_atm() 
        elif pilihan == "2":
            print("\nAnda memilih PENARIKAN TUNAI. Silakan pilih jumlah uang.")
            self.pilih_pecahan() 
        elif pilihan == "3":
            print("\nAnda memilih TRANSFER. Silakan masukkan nomor rekening tujuan.")
            self.kartu.transfer()
            self .menu_atm()
        elif pilihan == "4":
            print("\nAnda memilih PEMBAYARAN. Silakan pilih jenis pembayaran.")
            self.pembayaran()
        elif pilihan == "5":
            print("\nAnda memilih GANTI PIN. Silakan masukkan PIN baru.")
            self.kartu.gantiPin()
            self.tampilkan_pesan()
        elif pilihan == "6":
            print("\nAnda memilih FLazz. Silakan pilih fitur kartu Flazz.")
            self.list_flazz()
            self.menu_atm()
        elif pilihan == "7":
            print("\nAnda memilih SETOR TUNAI. Silakan masukkan uang ke mesin.")
            self.setor_tunai()
        elif pilihan == "cancel" or pilihan == "CANCEL":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.tampilkan_kartu()
        else:
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.menu_atm()

    def pilih_pecahan(self):
        if self.kartu.saldo <= 0:
            print("\nAnda tidak memiliki uang. Silahkan kerja dulu.")
            self.menu_atm()
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
            self.menu_atm()
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
            self.menu_atm()
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
            self.menu_atm() 
        else:
            self.kartu.saldo -= jumlah_tagihan
            print(f"\nPembayaran tagihan {jenis_tagihan} sebesar Rp {jumlah_tagihan:,} berhasil!")
            print(f"Sisa saldo Anda: Rp {self.kartu.saldo:,}")
            self.selesai_transaksi()
    
    def list_flazz(self):
        print("\n====================================")
        print("         Pilih FLAZZ                 ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("")
        
        dummyIndex = 1
        for kartu in list_flazz_obj:
            print(dummyIndex,". Nomor: ", kartu.nomorRekening, "Bank: ", kartu.bank, "Saldo: ", kartu.saldo)
            dummyIndex = dummyIndex + 1
        selected = input("Pilih Nomor Kartu: ")
        self.flazz = list_flazz_obj[int(selected)-1]

        pilihan = self.menu_kartu(self.flazz)

        if pilihan == "1":
            print("\nAnda memilih INFORMASI. Menampilkan informasi rekening...")
            self.flazz.informasi()
            self.menu_atm() 
        elif pilihan == "2":
            print("\nAnda memilih PENARIKAN TUNAI. Silakan pilih jumlah uang.")
            self.top_up_flazz()
            self.menu_atm()
        
    def top_up_flazz(self):
        print("\n====================================")
        print("         TOP UP SALDO FLAZZ        ")
        print("====================================")
        print("Untuk membatalkan transaksi, ketik 'CANCEL'")
        print("")
        
        jumlah_top_up = input("Masukkan jumlah top-up: ").strip()
        
        if jumlah_top_up.lower() == "cancel":
            print("\nTransaksi dibatalkan. Kembali ke menu utama.")
            self.menu_atm()
            return
        
        if not jumlah_top_up.isdigit():
            print("\nMasukan tidak valid. Silakan coba lagi.")
            self.top_up_flazz()
            return
        
        jumlah_top_up = int(jumlah_top_up)
        
        if self.kartu.saldo < jumlah_top_up:
            print("\nTop-up gagal! Saldo Anda tidak mencukupi, Silahkan Liat Saldo Anda Lagi.")
            self.top_up_flazz()
        else:
            # self.kartu.top_up(jumlah_top_up)
            self.kartu.saldo = self.kartu.saldo - jumlah_top_up
            self.flazz.saldo = self.flazz.saldo + jumlah_top_up
            print(f"\nTop-up Rp {jumlah_top_up:,} berhasil!")
            print(f"Sisa saldo Anda: Rp {self.kartu.saldo:,}")
            print(f"Sisa saldo Flazz: Rp {self.flazz.saldo:,}")
            self.menu_atm()

list_kartu_atm = [
    KartuATM("1234567890", "BCA",  2000000, "12/25" ,"123456", "PUnn_Doaa"),
    KartuATM("1235645390", "BCA", 2000000, "12/25", "808080", "Jon_Doss"),
    KartuATM("1213564530", "BCA", 2000000, "12/25", "232323", "Kukki_Doss")
]

list_flazz_obj = [
    Flazz("1090923223", "Flazz", 50000),
    Flazz("2240923353", "Flazz", 100000),
    Flazz("2444092753", "Flazz", 150000)
]

atm1 = ATM("BCA", 100000)

atm1.tampilkan_kartu()