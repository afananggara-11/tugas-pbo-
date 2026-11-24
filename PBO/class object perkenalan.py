class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Hallo nama saya {self.nama}")

    def hello(self, hello):
        print(f"Halo {hello}, nama saya {self.nama}")

mahasiswa = Mahasiswa()
mahasiswa.nama = "Afan"
mahasiswa.perkenalan()
mahasiswa.hello("Rendi")