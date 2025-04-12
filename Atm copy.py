import tkinter as tk
from tkinter import messagebox

class Kartu:
    def __init__(self, pin, nama, nomorRekening, bank, expired, saldo=0):
        self.pin = pin
        self.nama = nama
        self.nomorRekening = nomorRekening
        self.bank = bank
        self.expired = expired
        self.saldo = saldo

    def autentikasi(self, input_pin):
        return input_pin == self.pin

class ATM:
    def __init__(self, bank, pecahan, kartu_obj):
        self.bank = bank
        self.pecahan = pecahan
        self.kartu = kartu_obj
        self.saldo = kartu_obj.saldo  # Initialize ATM's saldo with Kartu's saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        self.kartu.saldo += jumlah  # Update Kartu's saldo as well
        return f"Setor tunai berhasil. Saldo baru Anda: Rp {self.saldo:,.2f}"

    def penarikan_tunai(self, jumlah):
        if jumlah > self.saldo:
            return "Saldo tidak mencukupi."
        else:
            self.saldo -= jumlah
            self.kartu.saldo -= jumlah  # Update Kartu's saldo as well
            return f"Penarikan berhasil. Sisa saldo Anda: Rp {self.saldo:,.2f}"

    def tampil_saldo(self):
        return f"Saldo Anda saat ini: Rp {self.saldo:,.2f}"

class ATM_GUI:
    def __init__(self, atm):
        self.atm = atm
        self.window = tk.Tk()
        self.window.title("ATM Machine")

        self.label = tk.Label(self.window, text="Selamat Datang di ATM!")
        self.label.pack()

        self.pin_label = tk.Label(self.window, text="Masukkan PIN:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self.window, show="*")
        self.pin_entry.pack()

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def login(self):
        pin = self.pin_entry.get()
        if self.atm.kartu.autentikasi(pin):
            self.result_label.config(text="Login Berhasil!")
            self.show_menu()
        else:
            self.result_label.config(text="PIN Salah!")

    def show_menu(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.window, text="Pilih Transaksi:")
        self.label.pack()

        self.saldo_button = tk.Button(self.window, text="Cek Saldo", command=self.cek_saldo)
        self.saldo_button.pack()

        self.setor_button = tk.Button(self.window, text="Setor Tunai", command=self.setor_tunai_window)
        self.setor_button.pack()

        self.tarik_button = tk.Button(self.window, text="Tarik Tunai", command=self.tarik_tunai_window)
        self.tarik_button.pack()

        self.exit_button = tk.Button(self.window, text="Keluar", command=self.window.destroy)
        self.exit_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def cek_saldo(self):
        saldo = self.atm.tampil_saldo()
        self.result_label.config(text=saldo)

    def setor_tunai_window(self):
        setor_window = tk.Toplevel(self.window)
        setor_window.title("Setor Tunai")

        jumlah_label = tk.Label(setor_window, text="Masukkan Jumlah Setoran:")
        jumlah_label.pack()
        jumlah_entry = tk.Entry(setor_window)
        jumlah_entry.pack()

        def setor():
            try:
                jumlah = float(jumlah_entry.get())
                result = self.atm.setor_tunai(jumlah)
                self.result_label.config(text=result)
                setor_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Jumlah tidak valid.")

        setor_button = tk.Button(setor_window, text="Setor", command=setor)
        setor_button.pack()

    def tarik_tunai_window(self):
        tarik_window = tk.Toplevel(self.window)
        tarik_window.title("Tarik Tunai")

        jumlah_label = tk.Label(tarik_window, text="Masukkan Jumlah Penarikan:")
        jumlah_label.pack()
        jumlah_entry = tk.Entry(tarik_window)
        jumlah_entry.pack()

        def tarik():
            try:
                jumlah = float(jumlah_entry.get())
                result = self.atm.penarikan_tunai(jumlah)
                self.result_label.config(text=result)
                tarik_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Jumlah tidak valid.")

        tarik_button = tk.Button(tarik_window, text="Tarik", command=tarik)
        tarik_button.pack()

    def run(self):
        self.window.mainloop()

# Example Usage
kartu1 = Kartu("123456", "John Doe", "1234567890", "BCA", "12/25", 1000000)
atm1 = ATM("BCA", 50000, kartu1)

gui = ATM_GUI(atm1)
gui.run()