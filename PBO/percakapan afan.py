class Pembeli:
    nama = ""
    ukuran = 0

    def dialog_1_sapaan(self):
        print(f"\n{self.nama}: Assalamu'alaikum, Mas. Nama saya {self.nama}.")
        print("Saya mendapat informasi kalau Mas punya sepatu futsal yang mau dijual.")

    def dialog_3_tanya_info(self, penjual):
        print(f"\n{self.nama}: Saya mau tanya-tanya tentang sepatu futsal yang dibawa, {penjual}.")
        print("Kira-kira merek dan tipenya apa saja yang tersedia, dan ukuran berapa?")

    def dialog_5_cek_fisik(self):
        print(f"\n{self.nama}: Saya mencari sepatu yang kondisinya masih bagus,")
        print(f"solnya belum aus, dan lem-lemannya masih kuat. Ukuran {self.ukuran} ini pas di saya.")
        print("Boleh saya cek kelenturan sol dan fitting-nya langsung?")

    def dialog_7_tanya_box(self):
        print(f"\n{self.nama}: Wah, bahannya lentur dan nyaman. Kotak (box) aslinya apakah masih lengkap?")
        print("Saya juga ingin memastikan apakah solnya cocok untuk lapangan interlock.")

    def dialog_9_tanya_harga(self):
        print(f"\n{self.nama}: Kalau untuk kisaran harganya berapa, Mas?")
        print("Apakah masih bisa nego tipis setelah cek barang seperti ini?")

    def dialog_11_tindak_lanjut(self):
        print(f"\n{self.nama}: Baik, saya tidak ingin buru-buru.")
        print("Yang penting kondisi sepatu sesuai dengan foto dan harganya masuk akal.")

    def dialog_13_pembayaran(self):
        print(f"\n{self.nama}: Untuk pembayarannya nanti bisa tunai langsung atau transfer m-banking, Mas?")

    def dialog_15_penutup(self, penjual):
        print(f"\n{self.nama}: Baik, lebih fleksibel ya. Terima kasih infonya, {penjual}.")
        print("Assalamu'alaikum.")


class Penjual:
    nama = ""
    lokasi = ""

    def dialog_2_sambut(self, pembeli):
        print(f"\n{self.nama}: Wa'alaikumsalam, {pembeli}!")
        print("Iya, benar. Saya memang sedang menawarkan beberapa pasang sepatu futsal.")
        print("Silakan, kita ngobrol dulu sambil lihat barangnya.")

    def dialog_4_jelaskan_sepatu(self):
        print(f"\n{self.nama}: Untuk saat ini ada merek Nike dan Adidas dengan kondisi yang masih mulus.")
        print("Nanti {pembeli} bisa melihat dan mengecek langsung supaya lebih yakin.")

    def dialog_6_izin_coba(self, pembeli):
        print(f"\n{self.nama}: Bisa banget, {pembeli}. Silakan dicoba dulu.")
        print("Mas bisa pakai kaos kaki untuk mencobanya langsung di tempat COD ini.")

    def dialog_8_jelaskan_sol(self):
        print(f"\n{self.nama}: Kotak aslinya masih lengkap saya simpan di rumah.")
        print("Solnya berjenis IN (Indoor), jadi sangat cocok untuk lapangan parquet atau interlock.")

    def dialog_10_jawab_harga(self):
        print(f"\n{self.nama}: Saya buka harga di angka yang tertera di iklan.")
        print("Tapi tenang, kalau sudah cocok kita bisa bicarakan sedikit penyesuaian harganya.")

    def dialog_12_setuju(self):
        print(f"\n{self.nama}: Setuju, Mas. Kita cari kesepakatan yang sama-sama enak.")
        print(f"Lokasi COD kita di {self.lokasi} ini juga sudah pas dan terang.")

    def dialog_14_opsi_bayar(self):
        print(f"\n{self.nama}: Bisa tunai langsung saat ini atau transfer m-banking,")
        print("mana saja yang lebih gampang dan nyaman buat Mas.")

    def dialog_16_perpisahan(self, pembeli):
        print(f"\n{self.nama}: Wa'alaikumsalam.")
        print(f"Hati-hati di jalan ya, {pembeli}. Semoga sepatunya awet dan makin semangat main futsalnya.")


# Inisialisasi Objek Pembeli (Afan)
afan = Pembeli()
afan.nama = "Afan"
afan.ukuran = 42

# Inisialisasi Objek Penjual (Akhdan)
akhdan = Penjual()
akhdan.nama = "Akhdan"
akhdan.lokasi = "area publik minimarket terdekat"

# Menjalankan 16 Alur Dialog Percakapan COD
afan.dialog_1_sapaan()
akhdan.dialog_2_sambut(afan.nama)

afan.dialog_3_tanya_info(akhdan.nama)
akhdan.dialog_4_jelaskan_sepatu()

afan.dialog_5_cek_fisik()
akhdan.dialog_6_izin_coba(afan.nama)

afan.dialog_7_tanya_box()
akhdan.dialog_8_jelaskan_sol()

afan.dialog_9_tanya_harga()
akhdan.dialog_10_jawab_harga()

afan.dialog_11_tindak_lanjut()
akhdan.dialog_12_setuju()

afan.dialog_13_pembayaran()
akhdan.dialog_14_opsi_bayar()

afan.dialog_15_penutup(akhdan.nama)
akhdan.dialog_16_perpisahan(afan.nama)