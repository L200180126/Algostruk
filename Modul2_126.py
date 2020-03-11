#Nomor 1
class Pesan(object):
    def__init__(self,p):
        self.pesan = p

    def apakahTerkandung(self,cari):
        if cari in self.pesan:
            return True
        else :
            return False
        
    def cetakPesan(self):
        vokal = "aiueoAIUEO"
        hitung = 0
        for i in self.pesan:
            if i in vokal:
                hitung += 1
        return hitung
    def hitungKonsonan(self):
        vokal = "aiueoAIUEO"
        berapa = 0
        for i in self.pesan:
            if i not in vokal:
                berapa += 1
        return berapa
#Nomor2
    
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self):
        s = self.nama + ", NIM " + str(self.NIM)\
            + ", tinggal di " + self.kotaTinggal\
            + ", uang saku " + str(self.uangSaku)\
            + " tiap bulannya"
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print("saya baru saja makan", s, "sambil belajar")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, p):
        self.kotaTinggal = p

    def tambahUangSaku(self, k):
        self.uangSaku += k
#Nomor 3
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

x = input("Masukkan nama -> ")
z = input("Masukkan NIM -> ")
w = input("Masukkan kotaTinggal -> ")
v = input("Masukkan uangSaku -> ")
y = Mahasiswa(x, z, w, v)
return y
#Nomor 4
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def listKuliah(self):
        return self.listKuliah

    def ambilKuliah (self, matkul):
        self.listKuliah.append(matkul)
#Nomor 5
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def listKuliah(self):
        return self.listKuliah

    def hapusKuliah (self, matkul):
        self.listKuliah.remove(matkul)

    def ambilKuliah (self, matkul):
        self.listKuliah.append(matkul)
#Nomor 6

def Manusia (object):
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def ambilNama(self, nama):
        return self.nama

    def ambilUmur(self, umur):
        return self.umur

    def ambilAlamat(self, nama):
        return self.alamat

def siswaSMA(Manusia):
    def __init__(self, nama, noAbsen, kelas, jurusan):
        self.nama = nama
        self.noAbsen = absen
        self.kelas = kelas
        self.jurusan = jurusan

    def ambilNama(self, nama):
        return self.nama

    def ambilNoAbsen(self, noAbsen):
        return self.noAbsen

    def ambilKelas(self, kelas):
        return self.kelas
    
    def ambilJurusan(self, jurusan):
        return self.jurusan
#Nomor 7
def Manusia (object):
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def ambilNama(self, nama):
        return self.nama

    def ambilUmur(self, umur):
        return self.umur

    def ambilAlamat(self, nama):
        return self.alamat

class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self):
        s = self.nama + ", NIM " + str(self.NIM)\
            + ", tinggal di " + self.kotaTinggal\
            + ", uang saku " + str(self.uangSaku)\
            + " tiap bulannya"
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print("saya baru saja makan", s, "sambil belajar")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, p):
        self.kotaTinggal = p

    def tambahUangSaku(self, k):
        self.uangSaku += k

class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")

a = MhsTIF("Damar ", 4092, "Boyolali", 200000)
a.ambilNama() # from class Manusia
a.makan("roti") # from class Mahasiswa
a.ambilNIM() # from class Mahasiswa
a.ambilUangSaku() # from class Mahasiswa
a.katakanPy() # from class MhsTIF
